#!/bin/bash

# Récupérer les arguments
CLEAN_TEMP=$1
CLEAN_WINDOWS_TEMP=$2
CLEAN_PREFETCH=$3
CLEAN_UPDATE_CACHE=$4
CLEAN_LOGS=$5

# Nettoyer le dossier Temp si la case à cocher est cochée
if [ "$CLEAN_TEMP" -eq 1 ]; then
    echo "Cleaning Temp folder..."
    sudo rm -rf /var/tmp/*
fi

# Nettoyer le dossier Temp de Windows si la case à cocher est cochée
if [ "$CLEAN_WINDOWS_TEMP" -eq 1 ]; then
    echo "Cleaning Windows Temp folder..."
    sudo rm -rf /tmp/*
fi

# Nettoyer le dossier Prefetch si la case à cocher est cochée
if [ "$CLEAN_PREFETCH" -eq 1 ]; then
    echo "Cleaning Prefetch folder..."
    sudo rm -rf /var/log/apt/*
fi

# Nettoyer le cache de mise à jour si la case à cocher est cochée
if [ "$CLEAN_UPDATE_CACHE" -eq 1 ]; then
    echo "Cleaning Update Cache..."
    sudo apt-get clean
fi

# Nettoyer les logs si la case à cocher est cochée
if [ "$CLEAN_LOGS" -eq 1 ]; then
    echo "Cleaning Logs..."
    sudo journalctl --vacuum-time=7d
fi

echo "Cleaning completed."
