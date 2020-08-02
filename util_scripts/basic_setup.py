import subprocess


def install_basic_packages():
    subprocess.call("util_scripts/install_basic_packages.sh")


def install_docker_compose():
    subprocess.call(["util_scripts/install_docker_docker_compose.sh"])