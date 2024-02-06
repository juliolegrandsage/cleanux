#!/bin/bash

# Nettoyer le cache de Chromium
echo "Cleaning Chromium cache..."
chromium-browser --incognito --temp-profile about:settings/clearBrowserData &
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
