#!/usr/bin/env bash

# Get our IP
touch ~/ip
curl -s ifconfig.co -o ~/ip

# Get Mono
apt-get update
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
apt-get install apt-transport-https
echo "deb https://download.mono-project.com/repo/ubuntu stable-xenial main" | sudo tee /etc/apt/sources.list.d/mono-official-stable.list
apt-get update
apt-get -y install mono-complete
apt-get -y upgrade

# Setup Haasbot
mkdir ~/haasonline/
tar -zxvf /synced_folder/linux32.tar.gz -C ~/haasonline/
bash ~/haasonline/BetaUpdate.sh
bash ~/haasonline/Haasbot.sh
killall mono
rm /tmp/HTS.exe.lock

python3 /synced_folder/fix_settings.py
bash ~/haasonline/Haasbot.sh

# Open Haas ports
ufw allow 8090
ufw allow 8092

sleep 10

cat ~/ip

echo "Provisoned."

# mkdir /etc/nginx/
# touch /etc/nginx/.htpasswd
# echo -n 'slaman:' > /etc/nginx/.htpasswd

# netstat -an | grep "LISTEN"