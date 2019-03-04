yes Y | sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
yes Y | sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
yes Y | sudo apt-get install libxvidcore-dev libx264-dev
yes Y | sudo apt-get install libgtk2.0-dev libgtk-3-dev
yes Y | sudo apt-get install libatlas-base-dev gfortran
yes Y | sudo apt-get install python2.7-dev python3-dev

cd ~
wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.3.0.zip
unzip opencv.zip
wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.3.0.zip
unzip opencv_contrib.zip

wget https://bootstrap.pypa.io/get-pip.py
yes Y | sudo python get-pip.py
yes Y | sudo python3 get-pip.py
