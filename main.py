from os import stat
import inotify.adapters
import subprocess
import paho.mqtt.client as mqtt
#from constants import SERVER, PORT, TIMEOUT

statuses = ["NOT_BUSY", "BUSY"]

client = mqtt.Client()

def mqtt_connect():
    client.connect(SERVER, port=PORT, keepalive=TIMEOUT)

def mqtt_send(current_status):
    pass

def cold_run_status_check():
    command = ["cat", "/proc/asound/card0/pcm0c/sub0/status"]
    command_run  = subprocess.Popen(command, stdout=subprocess.PIPE)
    try:
        output = subprocess.check_output(('grep', 'RUNNING'), stdin=command_run.stdout)
        current_status = statuses[1] # Busy
        print(f"Cold Run: {current_status}")
    except subprocess.CalledProcessError:
        current_status = statuses[0] # Not Busy
        print(f"Cold Run: 2 {current_status}")
    return current_status

def notifier_function():
    pass


def inotify_check():
    i = inotify.adapters.Inotify()
    i.add_watch('/dev/snd/pcmC0D0c')
    for event in i.event_gen(yield_nones=False):
        (_, type_names, path, filename) = event
        #print(f"PATH=[{path}] EVENT_TYPES={type_names}")
        if type_names == ['IN_OPEN']:
            current_status = statuses[1]
            print(f"{path} : {current_status}")
        elif type_names == ['IN_CLOSE_WRITE']:
            current_status = statuses[0]
            print(f"{path} : {current_status}")
    
        # type_names 'IN_OPEN' 'IN_CLOSE_WRITE'


def main():
    cold_run_status_check()
    inotify_check()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("CtrlC Interrupt. Exiting...")



