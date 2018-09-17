IO Pi Raspberry Pi with Expansion Board Python 3 Library
---
Python 3 Library to use the Raspberry Pi 3 Modell B+ 
(Computer-Board, BCM2837B0) and IO Pi Raspberry Pi expansion board 
from https://www.abelectronics.co.uk for reading all digitial input pins

The readme file for the extension board can be found at
https://github.com/abelectronicsuk/ABElectronics_Python3_Libraries/blob/master/IOPi/README.md

Install:
---
Download the library to your Raspberry Pi via terminal with: 

```
git clone https://github.com/TUM-E21-ThinFilms/rpidio
python3 rpidio/setup.py install
```

Packages ```RPi.GPIO``` and ``smbus`` need to be installed with:
```
apt-get install python3-pip
pip3 install RPi.GPIO
apt-get install python3-smbus
```

The included IO Pi library requires also i2c to be enabled.

Follow the tutorial at 
https://www.abelectronics.co.uk/i2c-raspbian-wheezy/info.aspx
to enable i2c for python 3.

Functions:
---
```
read(input):
```
Reads the status of a given input pin

**Parameter:** input - Use the constants from the class Inputs

**Returns:** a boolean

```
read_all():
```
reads the status of all input pins

**Returns:** an integer - the first 16 bit represents the extensionboard 1 port 1 pins, followed by 16 bits for port 2, and then finally the last 26 bits represent the mainboard GPIO pins
