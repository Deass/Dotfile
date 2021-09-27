#!/bin/sh

#pkill -f "dwmbar"; dwmbar &
pkill -f "dwmblocks"; dwmblocks &
pkill -f "sxhkd"; sxhkd -c ~/.config/sxhkd/sxhkdrc-dwm &
#pkill -f "dunst"; dunst -config ~/.config/dunst/dunstrc &
#pkill -f "unclutter"; unclutter --timeout 3 &
#pkill -f "notify-hightemp"; notify-hightemp &
#pkill -f "bash /usr/bin/clipmenud"; pkill -f "clipnotify"; clipmenud &
#pkill -f "flameshot"; flameshot &
#pkill -f "xcompmgr"; xcompmgr &
#pkill -f "lxpolkit"; lxpolkit &
pkill -f "picom"; picom -f &

