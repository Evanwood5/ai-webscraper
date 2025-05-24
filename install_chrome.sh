#!/bin/bash

# Install Google Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt-get update
apt-get install -y ./google-chrome-stable_current_amd64.deb

# Get matching ChromeDriver version
CHROME_VERSION=$(google-chrome --version | cut -d ' ' -f3 | cut -d '.' -f1)
wget -N https://chromedriver.storage.googleapis.com/$CHROME_VERSION/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
chmod +x chromedriver
mv -f chromedriver /usr/local/bin/chromedriver