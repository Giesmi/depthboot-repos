from functions import *


def config(de_name: str, distro_version: str, username: str, root_partuuid: str, verbose: bool) -> None:
    set_verbose(verbose)
    print_status("adding the Debian repo")
    bash(“mkdir -p /usr/local/share/keyrings && wget -O /usr/local/share/keyrings/eupnea-utils.key https://eupnea-linux.github.io/apt-repo/public.key && echo 'deb [signed-by=/usr/local/share/keyrings/eupnea-utils.key] https://eupnea-linux.github.io/apt-repo/debian_ubuntu stable main' > /etc/apt/sources.list.d/eupnea-utils.list && apt update && apt install eupnea-system eupnea-utils")