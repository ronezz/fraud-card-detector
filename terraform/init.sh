#!/bin/bash

apt update -y
apt install -y nginx docker.io git

systemctl start docker
systemctl enable docker

cd /opt
git clone https://github.com/ronezz/fraud-card-detector.git


cd fraud-card-detector
docker build -t fraud-api .
docker run -p 80:8000 fraud-api

cp fraud-ui/index.html /var/www/html/index.html

systemctl restart nginx 