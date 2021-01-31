# Mounting Pressure

This repository consists of a simple python program, a Processing script, along with a bash script, all intended to work together to create an appealing generative art experience. This program uses a monitor and a Neopixel module to generate a colorful ball display and a randomized LED activation system. When connected to a monitor, balls of various shapes and sizes spawn onscreen with a random direction and velocity, and interact both with other balls and the borders of the screen. When the Neopixel is hooked up, every 3 seconds there is the possibility for 1 of 8 LEDS to turn red, and every 24 seconds the Neopixel module resets itself to white. 
    
[Video Demo](https://youtu.be/KNExLvp8t4w)

# Table of Contents <!-- omit in toc -->
- [Setup](#setup)
  - [Hardware](#hardware)
  - [Software ](#software)
  - [LOTR API](#lotr-api)
  - [Running manually](#running-manually)
  - [Run on boot](#run-on-boot)

# Setup
## Hardware

This program requires a Raspberry Pi 3b+ running Raspbian GNU/Linux version 10+, aka buster. This also requires a monitor with an HDMI port and an 8 LED Neopixel module, similar to the one that comes in the Freenove Ultimate Starter kit for the ESP32-WROVER.
The Neopixel module Connect the LED module to the Raspberry Pi's must be prepared in the following configuration. 
1. Connect module's 5V to Pi's 5V
2. Connect module's GND to Pi's GND
3. Connect module's Din to Pi's GPIO21. It was initially on GPIO18, but it was discovered to be buggy. 

The  [raspbery pi documentation](https://www.raspberrypi.org/documentation/usage/gpio/) is a good reference to explain what these pins mean, along with more information about the pi itself.

## Software 
Once the Neopixel module is connected, ensure that you have python 3, and then run the following commands on your pi:

```
sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
sudo python3 -m pip install --force-reinstall adafruit-blinka
```

These will allow the python program to actually interact with the Neopixel module, which is a large component of this program. 

Additionally, please install processing onto your raspberry pi. The [processing webpage](https://pi.processing.org/get-started/) has some very helpful information on that front. Alternatively, run the following command in your pi terminal:
```
curl https://processing.org/download/install-arm.sh | sudo sh
```

The `sketch.pde` file is used to control the visualizations on the external monitor, while the `scripty.py` file is used to control the LED's on the Neopixel module. 


## LOTR API

Currently, the `scripty.py` uses an api known as [The One API](https://the-one-api.dev/). This API allows a python script to query a database of Lord of the Rings information. This program specifically queries quotes from the Lord of the Rings trilogy. In the `active_led()` method, one of 3 ids are chosen, each referring to one particular film. A query is then made specifying that 10 quotes are requested from a particular film, and then of those 10 quotes, 1 is randomly chosen. The number of chars within this quote are counted, and the simple formula of `quoteSize % 8` is applied to determine which of the 8 pixels will be switched to red. The API key currently in use is my own, but it is a free API and I'm sure the devs will appreciate if you signed up on your own. 


## Running manually
To start the program, clone the repository at `https://github.com/Federickg23/generativeArt.git` and run the commands recommended in the [software](#software) section of this README. Enter the generativeArt folder and simply run `boot.sh`. It should start the Neopixel and soon after run the processing script.  

## Run on boot

To run on boot, use your favorite editor known as Vim. Type `sudo vim ~/.bashrc` and add the path to wherever boot.sh is. The paths in boot.sh are all absolute paths, so they may need to be edited to run on other systems, unless you have cloned this repository to the desktop folder of your raspberry pi. 
With the path to boot.sh now in your `~/.bashrc` file, it should run on boot whenever the terminal is opened. 