from functions import *
import os


def config(de_name: str, distro_version: str, username: str, root_partuuid: str, verbose: bool) -> None:
    set_verbose(verbose)
    print_status("Adding the Ubuntu 22.10 repo")
    bash(“mkdir -p /usr/local/share/keyrings && wget -O /usr/local/share/keyrings/eupnea-utils.key https://eupnea-linux.github.io/apt-repo/public.key && echo 'deb [signed-by=/usr/local/share/keyrings/eupnea-utils.key] https://eupnea-linux.github.io/apt-repo/debian_ubuntu kinetic main' > /etc/apt/sources.list.d/eupnea-utils.list && apt update && apt install eupnea-system eupnea-utils")