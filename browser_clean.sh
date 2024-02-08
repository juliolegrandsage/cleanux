
#!/bin/bash

# Vider le cache du navigateur spécifié en argument
clean_browser_cache() {
    local browser=$1
    case $browser in
        "firefox")
            echo "Cleaning Firefox cache..."
            rm -rf ~/.cache/mozilla/firefox/*.default*/cache2/*
            echo "Cache cleaned"
            ;;
        "brave")
            echo "Cleaning Brave cache..."
            rm -rf ~/.cache/BraveSoftware/Brave-Browser/Cache/*
            ;;
        "opera")
            echo "Cleaning Opera cache..."
            rm -rf ~/.cache/opera/Cache/*
            ;;
        "chromium")
            echo "Cleaning Chromium cache..."
            rm -rf ~/.cache/chromium/Default/Cache/*
            ;;
        *)
            echo "Unsupported browser: $browser"
            ;;
    esac
}

# Utilisation : ./clean_browser_cache.sh <navigateur>
# Exemple : ./clean_browser_cache.sh firefox
clean_browser_cache "$1"
