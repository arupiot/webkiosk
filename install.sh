gsettings set org.gnome.desktop.background picture-uri file:///home/iot/webkiosk/arup.png
gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-ac-timeout '0'
gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-battery-timeout '0'
gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-battery-type 'nothing'
gsettings set org.gnome.settings-daemon.plugins.power idle-dim-time '0'
gsettings set org.gnome.settings-daemon.plugins.power idle-dim 'false'
gsettings set org.gnome.desktop.screensaver lock-delay '0'
gsettings set org.gnome.desktop.screensaver lock-enabled 'false'
gsettings set org.gnome.desktop.notifications show-banners 'false'

sudo apt install unclutter chromium-browser xdotool

mkdir -p ~/.config/autostart/
cp RunKiosk.desktop ~/.config/autostart/
cp RunKiosk.desktop ~/Desktop/
