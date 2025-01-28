#!/bin/bash

URL="https://github.com/dword32bit/ReverseShellBuilder/releases/download/1.0/rebuild"
DEST="/usr/bin/rebuild"

REQUIRED_TOOLS=("xterm" "netcat" "ncat" "socat" "busybox" "rustcat" "pwncat")

# Function to check if the script is running as root
check_if_root() {
    if [ "$(id -u)" -ne 0 ]; then
        echo "This script must be run as root. Please use sudo."
        exit 1
    fi
}

# Check if the script is running as root
check_if_root

# Function to check and install required tools
check_and_install_tools() {
    for tool in "${REQUIRED_TOOLS[@]}"; do
        if ! command -v "$tool" &>/dev/null; then
            echo "$tool is not installed. Installing..."
            sudo apt-get install -y "$tool"
        else
            echo "$tool is already installed."
        fi
    done
}

# Install required tools
check_and_install_tools

# Install colorama via pip
pip install colorama --break-system-packages

# Download ReverseShellBuilder
echo "Downloading ReverseShellBuilder..."
curl -L $URL -o $DEST

# Make the file executable
echo "Making the file executable..."
chmod +x $DEST

# Verify the installation
if [ -f "$DEST" ]; then
    echo "ReverseShellBuilder installed successfully at $DEST"
else
    echo "Installation failed."
fi
