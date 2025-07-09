#!/bin/bash

# Crée un dossier pour stocker les pages HTML
mkdir -p fiches_plantes

# Chemin vers le fichier contenant les URLs (modifie si besoin)
URL_FILE="fiches_plantes_urls.txt"

# Lire chaque ligne du fichier et télécharger avec wget
while IFS= read -r url; do
  # Extraire ID et slug depuis l'URL
  filename=$(echo "$url" | awk -F'/' '{print $(NF-1)"-"$NF".html"}')
  wget -q -O "fiches_plantes/$filename" "$url"
  echo "Téléchargé: $filename"
done < "$URL_FILE"
