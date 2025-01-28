# ReverseShellBuilder (Rebuild)

ReverseShellBuilder (Rebuild) is a tool designed to create various types of reverse shell payloads and execute them on a specified listener. The tool supports a variety of listeners such as `nc`, `ncat`, `socat`, `rustcat`, and more. You can use this tool to listen for connections from the target system once a reverse shell has been successfully executed.

## Features
- Provides various reverse shell payloads for different listener types.
- Supports multiple listener tools such as `nc`, `ncat`, `socat`, `rustcat`, `pwncat`, and others.
- Offers the ability to generate interactive TTY shell payloads.
- Saves and loads existing listener sessions.

## Installation

To install **ReverseShellBuilder**, you can use the provided automated installation script, `reverseshell_installer.sh`. This script will download the tool, move it to `/usr/bin/`, and ensure that all required dependencies are installed.

### Installation Steps

1. **Download the Installer Script**

   First, download and make the `reverseshell_installer.sh` script executable:

   ```bash
   wget https://raw.githubusercontent.com/dword32bit/ReverseShellBuilder/refs/heads/main/reverseshell_installer.sh
   chmod +x reverseshell_installer.sh
   ```

2. **Run the Installer Script**

   After making the script executable, run the installer with root privileges:

   ```bash
   sudo ./reverseshell_installer.sh
   ```

   The script will perform the following actions:
   - Check if the required tools (`xterm`, `netcat`, `ncat`, `socat`, `busybox`, `rustcat`, `pwncat`) are already installed.
   - Install any missing tools.
   - Download and move the `rebuild` file to `/usr/bin/`.
   - Ensure the `rebuild` file is executable.

### System Requirements
- Linux-based system (Debian/Ubuntu recommended).
- Root access for installation and configuration.
- An internet connection to download the required tools and dependencies.

### Using ReverseShellBuilder

Once the installation is complete, you can run **ReverseShellBuilder** by typing the following command:

```bash
rebuild
```

The program will display a menu that allows you to:
1. Configure the IP address and port for the listener.
2. Select which listener to use.
3. View and choose various reverse shell payloads to use.

### Uninstallation

To remove **ReverseShellBuilder**, you can run the following uninstaller script:

1. **Download the Uninstaller Script**

   ```bash
   wget https://example.com/path/to/uninstaller.sh
   chmod +x uninstaller.sh
   ```

2. **Run the Uninstaller Script**

   Run the uninstaller with root privileges to remove the tool:

   ```bash
   sudo ./uninstaller.sh
   ```

   The script will remove the `rebuild` file from `/usr/bin/` without affecting any other tools or dependencies.

## Contributing

If you'd like to contribute to this project, feel free to submit a pull request on GitHub. Please follow the development guidelines.

## Author
dword32bit
