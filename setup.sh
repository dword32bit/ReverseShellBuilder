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

# Function to install ReverseShellBuilder
install_rebuild() {
    echo "Installing required tools..."
    check_and_install_tools

    echo "Installing Python dependencies..."
    pip install colorama --break-system-packages

    echo "Downloading ReverseShellBuilder..."
    curl -L "$URL" -o "$DEST"

    echo "Making the file executable..."
    chmod +x "$DEST"

    if [ -f "$DEST" ]; then
        echo "ReverseShellBuilder installed successfully at $DEST"
        echo ""
	echo ""
	clear
	echo 'You can run "rebuild" from your terminal now!!!'
    else
        echo "Installation failed."
    fi
}

# Function to repair installation
repair_rebuild() {
    echo "Repairing installation..."
    install_rebuild
}

# Function to check for updates
check_update() {
    echo "Checking for updates..."
    curl -I "$URL" &>/dev/null
    if [ $? -eq 0 ]; then
        echo "Update available. Reinstalling..."
        install_rebuild
    else
        echo "No updates available."
    fi
}

# Function to uninstall ReverseShellBuilder
uninstall_rebuild() {
    echo "Uninstalling ReverseShellBuilder..."
    if [ -f "$DEST" ]; then
        rm -f "$DEST"
        echo "ReverseShellBuilder removed successfully."
    else
        echo "ReverseShellBuilder is not installed."
    fi
}

# Main menu function
main_menu() {
    art=(
        "\033[32m    ____                               \033[0m\033[31m    _____ __         ____\033[0m"
        "\033[32m   / __ \\\___ _   _____  _____________ \033[0m\033[31m    / ___// /_  ___  / / /\033[0m"
        "\033[32m  / /_/ / _ \\ | / / _ \\/ ___/ ___/ _ V\033[0m\033[31m    \\__ \/ __ \/ _ \/ / / \033[0m"
        "\033[32m / _, _/  __/ |/ /  __/ /  (__  )  __/ \033[0m\033[31m   __/ / / / /  __/ / /  \033[0m"
        "\033[32m/_/ |_|\\___/|___/\\___/_/  /____/\\___/\033[0m\033[31m   /____/_/ /_/\\___/_/_/   \033[0m"
        "\033[32m                            ____        _ __    __         \033[0m"
        "\033[32m                           / __ )__  __(_) /___/ /__  _____\033[0m"
        "\033[32m                          / __  / / / / / / __  / _ \\/ ___/\033[0m"
        "\033[32m                         / /_/ / /_/ / / / /_/ /  __/ /    \033[0m"
        "\033[32m                        /_____/\\__,_/_/_/\\__,_/\\___/_/ \033[0m\033[31m(v1.0)\033[0m"
        "\033[34m                                         by: dword32bit\033[0m"
    )

    for line in "${art[@]}"; do
        echo -e "$line"
    done

    echo "Select an option:"
    echo "1. Install"
    echo "2. Repair"
    echo "3. Check Update"
    echo "4. Uninstall"
    echo "5. Exit"
    read -rp "Enter your choice [1-5]: " choice

    case $choice in
        1)
            install_rebuild
            ;;
        2)
            repair_rebuild
            ;;
        3)
            check_update
            ;;
        4)
            uninstall_rebuild
            ;;
        5)
            echo "Exiting..."
            exit 0
	    clear
            ;;
        *)
            echo "Invalid choice. Please try again."
            main_menu
            ;;
    esac
}

# Run the main menu
main_menu
