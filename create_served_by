#!/usr/bin/env bash
# This is a script that install and configure nginx

#update ubuntu package and install nginx
sudo apt-get update
sudo apt-get install nginx -y

#create directories to be used in the project
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

#create a html page with "Holberton school" as body
echo "<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

#create a symbolic link to connect directories
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#changing directory ownership and permissions
sudo chown -R ubuntu:ubuntu /data/

#setting up the page to be served to the client upon request
sudo sed -i '/server_name _;/a \ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-available/default

#restart nginx the server
sudo service nginx restart
