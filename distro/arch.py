from functions import *


def config(verbose: bool) -> None:
    set_verbose(verbose)
    print_status("Adding the Arch repo")
    # Apply temporary fix for pacman
    bash("wget -O /tmp/eupnea.key https://eupnea-linux.github.io/arch-repo/public_key.gpg && sudo pacman-key --add /tmp/eupnea.key && sudo pacman-key --lsign-key 94EB01F3608D3940CE0F2A6D69E3E84DF85C8A12 && echo "[eupnea]"$'\n'"Server = https://eupnea-linux.github.io/arch-repo/$repo/os/any" | sudo tee -a /etc/pacman.conf && sudo pacman -Syy && sudo pacman -S eupnea-utils eupnea-system")
