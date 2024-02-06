#!/bin/bash

# Nettoyer le cache d'Opera
echo "Cleaning Opera cache..."
opera --new-private-tab about:settings/clearBrowserData &
sleep 2
xdotool key Tab Return
sleep 1
xdotool key Tab Return
sleep 1
xdotool key Tab Return
sleep 1
xdotool key Tab Return
sleep 1
xdotool key Return
sleep 1
xdotool key alt+f4
