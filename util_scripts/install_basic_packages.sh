#!/bin/bash
apt-get update
apt-get upgrade -y
apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common \
    python3-pip \
    wget \
    make \
    nano \
    gpg \
    python-gpg \
    python-certbot-nginx \
    htop
pip3 install mako
pip3 install click