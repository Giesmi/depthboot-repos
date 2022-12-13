#!/usr/bin/env python3

from typing import Tuple
from urllib.request import urlretrieve, urlopen
from urllib.error import URLError
import json

from functions import *

    # install arch-chroot for arch
    if de_name == "arch" and not path_exists("/usr/bin/arch-chroot"):
        print_status("Installing arch-chroot")
        if path_exists("/usr/bin/apt"):
            bash("apt-get install arch-install-scripts -y")
        elif path_exists("/usr/bin/pacman"):
            bash("pacman -S arch-install-scripts --noconfirm")
        elif path_exists("/usr/bin/dnf"):
            bash("dnf install arch-install-scripts --assumeyes")
        elif path_exists("/usr/bin/zypper"):  # openSUSE
            bash("zypper --non-interactive install arch-install-scripts")
        else:
            print_warning("Arch-install-scripts not found, please install it using your distros package manager or "
                          "select another distro instead of arch")
            exit(1)




# download the distro rootfs
def download_rootfs(distro_name: str) -> None:
    try:
        match distro_name:
            case "ubuntu":
                print_status("Debug text")
            case "debian":
                print_status("Debug text")
            case "arch":
                print_status("Debug text")
            case "fedora":
                print_status(f"Debug text")
            case "pop-os":
                print_status(f"Debug text")
    except URLError:
        print_error("Couldn't download rootfs. Check your internet connection and try again. If the error persists, "
                    "create an issue with the distro and version in the name")
        exit(1)


        print_status("Distro agnostic configuration complete")

# chroot command
def chroot(command: str) -> str:
    return bash(f'chroot /mnt/depthboot /bin/bash -c "{command}"')


# The main build script
def start_build(verbose: bool, local_path, kernel_type: str, dev_release: bool, build_options, img_size: int = 10,
                no_download_progress: bool = False, no_shrink: bool = False) -> None:
    if no_download_progress:
        disable_download_progress()  # disable download progress bar for non-interactive shells
    set_verbose(verbose)
    print_status("Starting build")

    prepare_host(build_options["distro_name"])

    match build_options["distro_name"]:
        case "ubuntu":
            import distro.ubuntu as distro
        case "debian":
            import distro.debian as distro
        case "arch":
            import distro.arch as distro
        case "fedora":
            import distro.fedora as distro
        case "pop-os":
            import distro.popos as distro
        case _:
            print_error("DISTRO NAME NOT FOUND! Please create an issue")
            exit(1)
    distro.config(verbose)

    post_config(build_options["distro_name"])

    print_header(f"The repo has been added! Please reboot your system for it to work")



if __name__ == "__main__":
    print_error("Do not run this file directly. Instead, run main.py")
