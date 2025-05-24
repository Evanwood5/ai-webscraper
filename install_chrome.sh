#!/bin/bash

# Download Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

# Extract it (Render doesn't support installing via apt)
dpkg-deb -x google-chrome-stable_current_amd64.deb $HOME/chrome

# Set CHROME path for Selenium
export CHROME_BIN=$HOME/chrome/opt/google/chrome/google-chrome

# Download ChromeDriver (match your local Chrome version, e.g., 124)
wget https://storage.googleapis.com/chrome-for-testing-public/124.0.6367.91/linux64/chromedriver-linux64.zip
unzip chromedriver-linux64.zip
mv chromedriver-linux64/chromedriver $HOME/chromedriver
chmod +x $HOME/chromedriver

# Add to PATH
export PATH=$HOME:$PATH