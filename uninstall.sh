#!/bin/bash

# Define the file to remove
DEST="/usr/bin/rebuild"

# Remove the file if it exists
if [ -f "$DEST" ]; then
    echo "Uninstalling ReverseShellBuilder..."
    rm -f $DEST
    echo "ReverseShellBuilder has been uninstalled."
else
    echo "ReverseShellBuilder is not installed."
fi
