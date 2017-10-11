#!/bin/bash

export DISPLAY=:0

unclutter &

sed -i 's/"exited_cleanly":false/"exited_cleanly":true/' /home/pi/.config/chromium/Default/Preferences
sed -i 's/"exit_type":"Crashed"/"exit_type":"Normal"/' /home/pi/.config/chromium/Default/Preferences

/usr/bin/chromium-browser --disable-translate --disable-infobars --touch-events=enabled \
    --disable-suggestions-service --disable-save-password-bubble --start-fullscreen \
    --start-maximised --kiosk --window-position=0,0 $1 &

while (true)
 do
  xdotool keydown ctrl; xdotool keyup ctrl;
  sleep 15
done
