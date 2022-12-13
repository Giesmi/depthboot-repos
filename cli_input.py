from getpass import getpass
from functions import *


def get_user_input(skip_device: bool = False) -> dict:
    output_dict = {
        "distro_name": ""
    }
    # Print welcome message
    print_header("The script will now ask a few questions. Once you are ready, just press 'enter' and"
                 " choose your distro.")
    input("(Press enter to continue)")
    print_question("Which distro will you add the repo to? Note: popOS is also Ubuntu 22.04")
    while True:
        temp_distro_name = input(
            "\033[94m" + "Available options: Pop!_OS/22.04, Ubuntu 22.10, Fedora, Debian, Arch\n" + "\033[0m")
        match temp_distro_name.lower():
            case "ubuntu":
                print("Ubuntu 22.10 selected")
                output_dict["distro_name"] = "ubuntu"
                break
            case "debian":
                    print("Debian stable selected")
                    output_dict["distro_name"] = "debian"
                    # TODO: Add non stable debian versions
                    break
            case "arch" | "arch btw":
                print("Arch selected")
                output_dict["distro_name"] = "arch"
                break
            case "fedora":
                print("Fedora selected")
                output_dict["distro_name"] = "fedora"
                break
            case "pop!_os" | "popos" | "pop_os | lts" | "":  # default
                print(“Pop!_OS/Ubuntu 22.04 selected")
                output_dict["distro_name"] = "pop-os"
                break
            case _:
                print_warning("Check your spelling and try again")
                continue

    print_status("User input complete")
    return output_dict
