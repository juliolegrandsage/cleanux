#!/bin/bash

# Nettoyer le cache de Brave
echo "Cleaning Brave cache..."
brave --new-window --incognito about:preferences#privacy &
sleep 2
xdotool key ctrl+shift+del
sleep 1
xdotool key Return
sleep 1
xdotool key Tab Return
sleep 1
xdotool key Tab Return
sleep 1
xdotool key Tab Return
sleep 1
xdotool key alt+f4
