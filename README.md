Real time number plate detection using openalpr
- opening a gate using arduino uno and python

- Debian 10 Buster Support

---------------------------------------------------
OPENALPR Compiling Instructions
---------------------------------------------------

//by yuxcat


prerequisites
```sh
sudo apt-get update
sudo apt-get upgrade ( proceed with caution : | upgrade all ur packages if the kernal fresh)
```

----------------------------
```sh
cd /usr/local/src
mkdir openalpr
```

//installing dependencies
```sh
sudo apt-get install --assume-yes libpng-dev libpng16-16 libjpeg62-turbo-dev libtiff-dev zlib1g-dev
sudo apt-get install --assume-yes build-essential
sudo apt-get install --assume-yes autoconf automake libtool
sudo apt-get install --assume-yes git-core
sudo apt-get install --assume-yes cmake
```

------------------------------------------------
//OpenCV

//OCV Dependencies
```sh
sudo apt-get install build-essential
sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libdc1394-22-dev
```
```sh
wget http://security.debian.org/debian-security/pool/updates/main/j/jasper/libjasper1_1.900.1-debian1-2.4+deb8u6_amd64.deb
sudo apt-get install libjasper1_1.900.1-debian1-2.4+deb8u6_amd64.deb
```

//gitclone ocv
```sh
git clone https://github.com/opencv/opencv.git

sudo apt-get install gtk+3.0
sudo apt-get install libavresample-dev
sudo apt-get install libgstreamer-plugins-base1.0-dev
```
 

//building
```sh
cd /opencv
mkdir release
cd release
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local ..

make
sudo make install
```

--------------------------------------
--------------------------------------

//leptonica
```sh
wget http://www.leptonica.org/source/leptonica-1.80.0.tar.gz

cd /usr/local/src/openalpr/leptonica-1.80/
chmod +x configure
./configure --prefix=/usr/local
make
sudo make install
```
---------------------------------------------
---------------------------------------------
//tesseract 3.04
```sh
cd /usr/local/src/openalpr
wget https://github.com/tesseract-ocr/tesseract/archive/3.04.00.tar.gz
mv tesseract to tesseract-ocr

./autogen.sh
chmod +x configure
./configure
make
sudo make install
sudo ldconfig
```
----------------------------------------------
----------------------------------------------

//gitclone openalpr
```sh
cd /usr/local/src/openalpr/

git clone https://github.com/openalpr/openalpr.git

```
nano CMakeLists.txt

add these lines
```sh
SET(OpenCV_DIR "/usr/local/lib")
SET(Tesseract_DIR "/usr/local/src/openalpr/tesseract-ocr")
```
//reqs
```sh
sudo apt-get install -y default-jdk
sudo apt-get install libcurl4-openssl-dev
sudo apt-get install liblog4cplus-dev
sudo apt-get install liblog4cplus-1.1-9
sudo apt-get install libjna-jni
```
```sh
cmake ./
make
sudo make install
```
```sh
sudo apt-get update
sudo apt-get upgrade
sudo apt autoremove

sudo apt install libcanberra-gtk-module
```
--caution------only run this if u get libopenalpr.so.2 errors -----
sudo apt-get install libopenalpr-dev
dont install other additional dependencies, just run and cancel
------------------------------------------

---------
```sh
pip install numpy

```

```sh


apt-get install libgstreamer1.0-0 gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-doc gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio
```
