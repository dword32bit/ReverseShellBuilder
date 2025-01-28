#!/bin/bash

URL="https://github.com/dword32bit/ReverseShellBuilder/releases/download/1.0/rebuild"
DEST="/usr/bin/rebuild"

REQUIRED_TOOLS=("xterm" "netcat" "ncat" "socat" "busybox" "rustcat" "pwncat")

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

check_and_install_tools
pip install colorama --break-system-packages

echo "Downloading ReverseShellBuilder..."
curl -L $URL -o $DEST

echo "Making the file executable..."
chmod +x $DEST

if [ -f "$DEST" ]; then
    echo "ReverseShellBuilder installed successfully at $DEST"
else
    echo "Installation failed."
fi
