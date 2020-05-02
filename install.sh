#!/bin/bash

# install stuff
apt update && apt -y upgrade && apt -y install python ffmpeg && pip install -U pip && pip install -U youtube-dl

# add update alias to bashrc
echo "alias update='apt update && apt -y upgrade && pip install -U pip && pip install -U youtube-dl'" >> ~/.bashrc; 

# setup termux storage
termux-setup-storage

# create dirs
mkdir -p ~/.config/youtube-dl
mkdir -p ~/bin
mkdir -p /data/data/com.termux/files/home/storage/downloads/music

# setup config
echo '-o "/data/data/com.termux/files/home/storage/downloads/music/%(title)s.%(ext)s" -x --audio-format mp3 -i' > ~/.config/youtube-dl/config

# setup url opener
echo '#!/bin/bash' > ~/bin/termux-url-opener
echo 'url=$1' >> ~/bin/termux-url-opener
echo 'youtube-dl $url' >> ~/bin/termux-url-opener
chmod +x ~/bin/termux-url-opener