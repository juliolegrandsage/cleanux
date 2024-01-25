#!/bin/bash
echo flow
# Nettoyage du cache apt
sudo apt-get clean
sudo apt-get autoclean

# Suppression des paquets inutiles
sudo apt-get autoremove

# Nettoyage du cache des vignettes
rm -r ~/.cache/thumbnails/*

# Nettoyage des journaux du système
sudo journalctl --vacuum-time=7d

# Suppression des fichiers temporaires
sudo rm -rf /tmp/*

# Nettoyage du cache des navigateurs web (exemple pour Firefox)
# Assurez-vous d'ajuster en fonction du navigateur que vous utilisez
rm -rf ~/.mozilla/firefox/*/Cache/*
rm -rf ~/.mozilla/firefox/*/OfflineCache/*

echo "Nettoyage terminé"