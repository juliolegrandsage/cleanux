#!/bin/bash
echo "1"
# Nettoyage du cache apt
sudo apt-get clean
sudo apt-get autoclean
echo "1"

# Suppression des paquets inutiles
sudo apt-get autoremove
echo "1"

# Nettoyage du cache des vignettes
rm -r ~/.cache/thumbnails/*
echo "1"

# Nettoyage des journaux du système
sudo journalctl --vacuum-time=7d
echo "1"

# Suppression des fichiers temporaires
sudo rm -rf /tmp/*
echo "1"

# Nettoyage du cache des navigateurs web (exemple pour Firefox)
# Assurez-vous d'ajuster en fonction du navigateur que vous utilisez
rm -rf ~/.mozilla/firefox/*/Cache/*
rm -rf ~/.mozilla/firefox/*/OfflineCache/*
echo "1"

echo "Nettoyage terminé"
