#!/bin/sh

userresources=$HOME/.Xresources
usermodmap=$HOME/.Xmodmap
sysresources=/etc/X11/xinit/.Xresources
sysmodmap=/etc/X11/xinit/.Xmodmap

# merge in defaults and keymaps

if [ -f $sysresources ]; then
    xrdb -merge $sysresources
fi

if [ -f $sysmodmap ]; then
    xmodmap $sysmodmap
fi

if [ -f "$userresources" ]; then
    xrdb -merge "$userresources"
fi

if [ -f "$usermodmap" ]; then
    xmodmap "$usermodmap"
fi

# start some nice programs

if [ -d /etc/X11/xinit/xinitrc.d ] ; then
 for f in /etc/X11/xinit/xinitrc.d/?*.sh ; do
  [ -x "$f" ] && . "$f"
 done
 unset f
fi

# Load Profile
[ -f ~/.profile ] && . ~/.profile

# Wallpapers
~/.fehbg

# Clipmenu Environment Variables
export CM_LAUNCHER=rofi-clipmenu
export CM_DIR=/tmp

# App
xrdb -merge .Xresources
#feh --bg-scale ./Pictures/wallpapers/BernkastelB.jpg &
picom -f &
sxhkd -c ~/.config/sxhkd/sxhkdrc-dwm &

# WM
#exec dwm
#exec bspwm

# DWM
while :; do
	ssh-agent dwm
done

