#!/bin/bash

# Fonction pour afficher la barre de progression
show_progress() {
    # Afficher la barre de progression avec zenity
    zenity --progress --title="Cleaning Progress" --text="Cleaning in progress..." --percentage=0 --auto-close --width=400
}

# Récupérer les arguments
CLEAN_TEMP=$1
CLEAN_WINDOWS_TEMP=$2
CLEAN_PREFETCH=$3
CLEAN_UPDATE_CACHE=$4
CLEAN_LOGS=$5

# Vérifier si les variables sont définies et sont des nombres entiers
if [[ -n "$CLEAN_TEMP" && "$CLEAN_TEMP" =~ ^[0-9]+$ ]]; then
    # Nettoyer le dossier Temp spécifique à Linux Mint si la case à cocher est cochée
    if [ "$CLEAN_TEMP" -eq 1 ]; then
        echo "Cleaning Linux Mint Temp folder..."
        sudo rm -rf /tmp/*
    fi
else
    echo "Error: CLEAN_TEMP is not defined or not an integer."
fi

if [[ -n "$CLEAN_MINT_TEMP" && "$CLEAN_MINT_TEMP" =~ ^[0-9]+$ ]]; then
    # Nettoyer le dossier Temp de Windows si la case à cocher est cochée
    if [ "$CLEAN_MINT_TEMP" -eq 1 ]; then
        echo "Cleaning Mint Temp folder..."
        sudo rm -rf /var/tmp/*
    fi
else
    echo "Error: CLEAN_MINT_TEMP is not defined or not an integer."
fi

if [[ -n "$CLEAN_PREFETCH" && "$CLEAN_PREFETCH" =~ ^[0-9]+$ ]]; then
    # Nettoyer le dossier Prefetch si la case à cocher est cochée
    if [ "$CLEAN_PREFETCH" -eq 1 ]; then
        echo "Cleaning Prefetch folder..."
        sudo rm -rf /var/log/apt/*
    fi
else
    echo "Error: CLEAN_PREFETCH is not defined or not an integer."
fi

if [[ -n "$CLEAN_UPDATE_CACHE" && "$CLEAN_UPDATE_CACHE" =~ ^[0-9]+$ ]]; then
    # Nettoyer le cache de mise à jour si la case à cocher est cochée
    if [ "$CLEAN_UPDATE_CACHE" -eq 1 ]; then
        echo "Cleaning Update Cache..."
        sudo apt clean
    fi
else
    echo "Error: CLEAN_UPDATE_CACHE is not defined or not an integer."
fi

if [[ -n "$CLEAN_LOGS" && "$CLEAN_LOGS" =~ ^[0-9]+$ ]]; then
    # Nettoyer les logs si la case à cocher est cochée
    if [ "$CLEAN_LOGS" -eq 1 ]; then
        echo "Cleaning Logs..."
        sudo journalctl --vacuum-time=7d
    fi
else
    echo "Error: CLEAN_LOGS is not defined or not an integer."
fi

# Appeler la fonction pour nettoyer le cache du navigateur
browser_cleaners/browser_clean.sh "$6"

echo "Cleaning completed."
