#!/usr/bin/env bash
cat >/etc/motd <<EOL
  _____
  /  _  \ __________ _________   ____
 /  /_\  \\___   /  |  \_  __ \_/ __ \
/    |    \/    /|  |  /|  | \/\  ___/
\____|__  /_____ \____/ |__|    \___  >
        \/      \/                  \/
A P P   S E R V I C E   O N   L I N U X
Documentation: http://aka.ms/webapp-linux
NodeJS quickstart: https://aka.ms/node-qs
Python quickstart> https://docs.microsoft.com/en-us/azure/app-service/containers/quickstart-python
EOL
cat /etc/motd

# SSH
service ssh start
python /code/manage.py migrate
python /code/manage.py collectstatic --noinput
. /entrypoint.sh  # the base docker's entrypoint
