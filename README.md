# ReverseShellBuilder (Rebuild)

ReverseShellBuilder (Rebuild) is a tool designed to create various types of reverse shell payloads and execute them on a specified listener. The tool supports a variety of listeners such as `nc`, `ncat`, `socat`, `rustcat`, and more. You can use this tool to listen for connections from the target system once a reverse shell has been successfully executed.
## Images
![image](https://github.com/user-attachments/assets/9238b762-b552-499b-8f82-98a3bf8262c7)
before install
------------
![image](https://github.com/user-attachments/assets/c4fe4a41-67c5-46a7-adbc-7ef49dec5e70)
installed


## Features
- Provides various reverse shell payloads for different listener types.
- Supports multiple listener tools such as `nc`, `ncat`, `socat`, `rustcat`, `pwncat`, and others.
- Offers the ability to generate interactive TTY shell payloads.
- Saves and loads existing listener sessions.

## Installation

To install **ReverseShellBuilder**, you can use the provided automated installation script, `setup.sh > install`. This script will download the tool, move it to `/usr/bin/`, and ensure that all required dependencies are installed.

### Setup

1. **Download the setup Script**

   First, download and make the `setup.sh` script executable:
   or you can clone my repo

   ```bash
   wget https://raw.githubusercontent.com/dword32bit/ReverseShellBuilder/refs/heads/main/setup.sh
   chmod +x setup.sh
   ```

3. **Run the setup Script**

   After making the script executable, run the installer with root privileges:

   ```bash
   sudo ./setup.sh
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

## Contributing

If you'd like to contribute to this project, feel free to submit a pull request on GitHub. Please follow the development guidelines.

## Author
dword32bit
