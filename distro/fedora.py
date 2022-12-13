from functions import *


def config(verbose: bool) -> None:
    set_verbose(verbose)
    print_status("Adding the Fedora repo")
    bash(“dnf config-manager --add-repo https://eupnea-linux.github.io/rpm-repo/eupnea-utils.repo && dnf check-update && dnf install eupnea-utils")
