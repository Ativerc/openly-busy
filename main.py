from os import stat
import inotify.adapters
import subprocess
import paho.mqtt.client as mqtt
#from constants import SERVER, PORT, TIMEOUT

statuses = ["NOT_BUSY", "BUSY", "APP_EXIT"]

mqttclient = mqtt.Client()


def mqtt_send(current_status):
    mqttclient.connect("localhost", port=1883, keepalive=60)
    mqttclient.publish("openbusylight/statuscode", payload=current_status, retain=True)

def main_notifier(listt):
    from_function = listt[0]
    current_status = listt[1]
    mqtt_send(current_status)
    print(f"{from_function}: {current_status}")

def cold_run_status_check():
    command = ["cat", "/proc/asound/card0/pcm0c/sub0/status"]
    command_run  = subprocess.Popen(command, stdout=subprocess.PIPE)
    try:
        output = subprocess.check_output(('grep', 'RUNNING'), stdin=command_run.stdout)
        current_status = statuses[1] # Busy
        main_notifier(["Cold Run", current_status])
    except subprocess.CalledProcessError:
        current_status = statuses[0] # Not Busy
        main_notifier(["Cold Run", current_status])
    return current_status

def inotify_check():
    i = inotify.adapters.Inotify()
    i.add_watch('/dev/snd/pcmC0D0c')
    for event in i.event_gen(yield_nones=False):
        (_, type_names, path, filename) = event
        #print(f"PATH=[{path}] EVENT_TYPES={type_names}")
        if type_names == ['IN_OPEN']:
            current_status = statuses[1]
            main_notifier([path, current_status])
        elif type_names == ['IN_CLOSE_WRITE']:
            current_status = statuses[0]
            main_notifier([path, current_status])
    
        # type_names 'IN_OPEN' 'IN_CLOSE_WRITE'


def main():
    cold_run_status_check()
    inotify_check()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        mqtt_send(statuses[2])
        print("CtrlC Interrupt. Exiting...")



