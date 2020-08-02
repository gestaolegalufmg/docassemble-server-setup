#!/bin/bash
apt-get update
apt-get upgrade -y
apt-get install -y \
    curl \
    python3-pip \
    wget \
    make \
    nano \
    htop
pip3 install mako
pip3 install click