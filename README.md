# openbusylight

## Pseudocode?
1. Check all of these:
  * mic-cam usage (this on its own is bad; if you are on a meeting and muted; someone looks at the busylight is off (because busylight is off) ; the person disturbs you
  * Meet/Teams/Zoom usage (only Teams provides an API to check if you're on a meeting yourself; only for Enterprise accounts though) THis is needed to be implemented. I would try to add Duo, WhatsApp and other apps call presence/usage as well.
  * User set variable (a software or hardware set variable which the user sets to sign that they are on a call)
2. Report to MQTT server
3. Change LED status
