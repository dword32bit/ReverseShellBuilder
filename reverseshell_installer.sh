#!/bin/bash

URL="https://github.com/dword32bit/ReverseShellBuilder/releases/download/1.0/rebuild"
DEST="/usr/bin/rebuild"

echo "Downloading ReverseShellBuilder..."
curl -L $URL -o $DEST



echo "Making the file executable..."
chmod +x $DEST

if [ -f "$DEST" ]; then
    echo "ReverseShellBuilder installed successfully at $DEST"
else
    echo "Installation failed."
fi
