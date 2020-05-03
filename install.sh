#!/bin/bash

# install stuff
apt update && apt -y upgrade && apt -y install python ffmpeg wget && pip install -U pip && pip install -U youtube-dl

# add update alias to bashrc
echo "alias update='apt update && apt -y upgrade && pip install -U pip && pip install -U youtube-dl'" >> ~/.bashrc; 

# setup termux storage
termux-setup-storage

# remove existing youtube-dl config if present
# CAUTION: If you depend on this - don't run this line!
rm -rf ~/.config/youtube-dl

# create bin directory
mkdir -p ~/bin

# setup url opener
echo '#!/bin/bash' > ~/bin/termux-url-opener
echo 'url=$1' >> ~/bin/termux-url-opener
echo 'python ~/dloader.py $url' >> ~/bin/termux-url-opener
chmod +x ~/bin/termux-url-opener

# download the downloader
curl https://raw.githubusercontent.com/aleksandarristic/ytdl/master/dloader.py -o ~/dloader.py