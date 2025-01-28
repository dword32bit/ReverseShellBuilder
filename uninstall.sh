#!/bin/bash

# Path to the installed file
DEST="/usr/bin/rebuild"

# Function to remove the installed file
remove_installed_file() {
    if [ -f "$DEST" ]; then
        echo "Removing ReverseShellBuilder from $DEST..."
        sudo rm -f "$DEST"
    else
        echo "ReverseShellBuilder not found at $DEST."
    fi
}

# Ensure the script is run as root
if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run as root. Please use sudo."
    exit 1
fi

# Remove the installed file
remove_installed_file

echo "Uninstallation complete."
