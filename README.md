# openly-busy
This tool lets people around you know if you are busy working/attending meetings/videocalls on your computer. 


**WARNING: This only works on my PC at the moment since I haven't been able to find a cross-platform library to report microphone/camera usage. If you can help me out regarding this, then please sound off in [this project's issues](https://github.com/Ativerc/openly-busy/issues)**

Checks the Microphone/Camera usage on your computer to check if you are busy. Acts as a MQTT client to disseminate your busy status to other devices.

Made for and tested on a Ubuntu 20.04 system. Other OS support soon.

# Installation:

## Dependencies:

1. Install `inotify` through `apt`:

    `sudo apt install inotify-tools`

2. Have a MQTT broker running on the network. Preferably locally.

    You can do `sudo apt install mosquitto` to install mosquitto MQTT broker.

3. Clone this repo

    `git clone https://github.com/Ativerc/openly-busy.git`

4. Make an env 

    `python3 -m venv env`

5. Install the pip dependencies using:

    `pip install -r requirements.txt`

# Issues:

See [Issues](https://github.com/Ativerc/openly-busy/issues).


## Pseudocode?
1. Check all of these:
  * mic-cam usage (this on its own is bad; if you are on a meeting and muted; busylight is hence off; the person disturbs you
  * Meet/Teams/Zoom usage/API (only Teams provides an API to check if you're on a meeting yourself; only for Enterprise accounts though) This needs to be implemented. I would try to add Duo, WhatsApp and other apps call presence/usage as well.
  * User set variable (a software or hardware set variable which the user sets to sign that they are on a call)
2. Report to MQTT server

## Ideas:
1. Someone made an Chrome extension for checking if a person is on a google meet meeting. Only works on Chrome though.
2. Someone made a busy-light by observing network packets. Well written code. But I feel observing mic usage will give a better check for whether if the user is busy. Say if the user is recording a video or audio, I feel monitoring mic usage would be better. 
