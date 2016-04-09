# 1 Sonifying Dirty Data
![The plan mapped out](https://i.imgur.com/DOmpxuk.png)

This project is an attempt to sonify dirty data. So much of Optical Character Recognition (OCR) focuses on, surprise, visuality. Digital Humanists are no strangers to cleaning up dirty data. We see it presented before us on screens. The OCR misses words, or replaces letters with numbers. We then use cleaning methods, regular expressions, and other tools to return the text to its original informational state. We clean away the 'nonsense' data that becomes entangled in our 'pure' data. But what happens if we sonify that dirty data? We challenge the idea that text is useless because it is 'dirty'. Take it a step further: what happens if we then convert that sonification back into a text file? We begin to mix the digital voice into our work. Sound literally changes our data as it becomes entangled in our association of OCR and visuality. Sonification complements and even enhances the purely visual aspect of OCR.

## 1.1 Bare Necessities
- Raspberry Pi 2 (preferably with plastic case)
- Raspberry Pi camera module
- Internet connection (only for the development stage) with ethernet cord or Wifi dongle
- Micro SD card with adapter
- Raspbian Jessie operating system image
- HDMI cable (**NOT** a [VGA cable since these do not output sound or connect to the Pi](https://en.wikipedia.org/wiki/VGA_connector))
- Headphones, speakers (that can plug into standard 1/8 inch jack), or TV/monitor (with speakers)
- Spare cardboard box, electrical and/or technical tape, exacto knife/box cutter
- 2 330 ohm resistors
- 2 LED Lights (1 red, 1 green)
- 3 male to male jumper cables
- 1 breadboard (get a mid-sized board to ensure enough space)
- 1 breakout cobbler (depending on your model, you can use a T-cobbler)
- 1 breakout ribbon

We will install the following software:
- Tesseract (Optical Character Recognition software)
- Alsa (Plays audio)
- Espeak (Speech recognition software for Text to Speech)
- Bison (Compiles Sphinx packages)
- SphinxBase (Speech recognition software for Speech to Text)
- PocketSphinx (Sphinx addon)
- Sox (Audio converter)

## 1.2 Important Note on Hardware
**CAUTION**: Make sure your Pi is completely shutdown and disconnected from power **before** attaching hardware components (camera, breadboard, wires, etc.).

For this tutorial, I used a Raspberry Pi 2 Model B. My Pi has a 40-pin breakout. Therefore, I used a 40 pin breakout ribbon and cobbler. Older Pi models use 26 pin breakouts. Check your model and hardware requirements. 

This tutorial assumes you are using a breakout ribbon and cobbler. **Be careful connecting pins and breakout components to your Pi and the breadboard**. However, do not be afraid to use a bit of force to connect the components. All pins must be fully inserted into their relevant components.

However, a breakout kit is not a requirement to create a functioning LED breadboard and will save you about $15-20. You can instead use female to male jumper cables: the female end connects to the Pi breakout and the male end connects to the breadboard. [This tutorial](https://projects.drogon.net/raspberry-pi/gpio-examples/tux-crossing/gpio-examples-1-a-single-led/) shows how to connect your Pi to the breadboard using only jumper cables. In this case you will need 2 female to male cables rather than two male to male cables. You also must note what numbers on the breadboard you are connecting to for the Python script in [section 1.9](#19-compare-text-files)

**If you use different hardware, your requirements WILL be different from mine**. 

**CAUTION: You need 2 330 ohm resistors for this project**. The resistors regulate the current to the LEDs so that they do not short or cause electrical issues with your Pi. 

## 1.3 Getting Started
Let's start from scratch. If you already have your Pi running, or are using a preinstalled SD card, you can skip to the [section 1.3.1](#131-the-screen-isnt-showing-your-pi-and-hdmi).

For this tutorial we are going to use the official Raspberry Pi operating system, Raspbian. You can install NOOBS, but all that does is give you a choice between several operating systems.

On the Raspberry Pi [downloads page](https://www.raspberrypi.org/downloads/raspbian/) select Raspbian and choose a version to download. If you have an 8GB Micro SD card, stick with Rapsbian Jessie. If you have a much smaller Micro SD card, you might choose Raspbian Jessie Lite since it is a more bare-bones version of Raspbian and thus uses less space. **This tutorial uses Raspbian Jessie 4.1** so use Lite at your own caution (though you should still be able to download packages and do most of the heavy lifting). Micro SD cards are relatively cheap, though, so think about purchasing a larger one if need be. 

**NOTE**: A Micro SD card is a small little chip. You usually cannot connect a Micro SD directly to your computer. Most Micro SD cards, however, come with an adapter. Plug the Micro SD into the adapter and make sure the little locking mechanism is unlocked (or else you cannot write anything to the card).

Once your image has downloaded, insert your Micro SD card in the adapter to your computer, and follow Raspberry Pi's [documentation on how to mount the image to your Micro SD card](https://www.raspberrypi.org/documentation/installation/installing-images/). Each platform has its own method. Remember to safely eject the card from your computer.

### 1.3.1 The Screen isn't Showing! Your Pi and HDMI
I am devoting an entire sub-section to connecting your Pi to a monitor via and HDMI cable because **this can be the most annoying first step for any Pi beginner.** 

Before plugging your Pi into the power, plug in your Micro SD card - the gold stripes should face the Pi and you will hear a click, locking the Micro SD card in place. 

Then turn your monitor on. Wait until it is running. Make sure your HDMI cable is connected to your monitor. **Now** plug in the HDMI cable to your Pi. If you do not have a device that supports HDMI, fear not.[ You can connect you Pi to your computer via an ethernet cable](https://www.raspberrypi.org/blog/use-your-desktop-or-laptop-screen-and-keyboard-with-your-pi/). **YOU CANNOT CONNECT YOUR PI TO YOUR COMPUTER VIA HDMI**, since your computer's HDMI is usually an output, not an input.

**NOTE**: Your monitor, TV, etc. may have multiple HDMI inputs. Thankfully, these are usually numbered to correspond with the inputs HDMI channel on, say your TV. Make sure you note which input you are using on the monitor. Switch to that input. For example, I have plugged my HDMI cable into my TV into the HDMI 2 input, so now I have to change the TV's input to HDMI 2 (usually by hitting the source or input button on your remote until you hit it. 

Plug your Pi into its power source and wait for it to boot. If all goes well, you will see a rainbow image and then a ton of code running on the screen while it boots. 

**NOTE**: If you see nothing and you followed the set-up, you may have to change some code in the `config.txt` file. See Raspberry Pi's documentation for [more information on](https://www.raspberrypi.org/documentation/configuration/config-txt.md) `config.txt`.

You should now see your Pi's desktop. Make sure you have a mouse and keyboard plugged into your Pi. Explore around a bit. You can play games, use some interesting tools, etc.

Lastly, make sure to connect to the internet. If you have purchased a Wifi dongle with your Pi (it looks like a little USB stick), plug that into your Pi. To connect to Wifi, select the network symbol in the top right of the screen. Select your Wifi network and enter your password.

Otherwise, connect your Pi directly to one of your router's ethernet ports (I use port number 4) with your ethernet cable. 

## 1.4 Update your Pi
Now that your Pi is up and running, open your Pi's terminal (command line).

**NOTE**: You can also run your Pi directly from your own computer using a secure shell or SSH. This is a very simple method to run your Pi from your own computer's command line. See Raspberry Pi's [documentation on SSH](https://www.raspberrypi.org/documentation/remote-access/ssh/). This is purely preference. SSH-ing is pretty darn cool and can help if you don't want cords running every which way out of your Pi. I prefer using the Pi's terminal.

Although you have the latest operating system image, you will still need to upgrade your packages since many have had updates since the original operating system was written and published. To do this, you will need to run two commands integral to Linux operating systems (which Pi is based off of):

`sudo apt-get update` grabs all of the packages to keep your system updated.
`sudo apt-get upgrade` extracts and installs the downloaded packages.

**NOTE**: You will be running these commands as the administrator or 'superuser' using the UNIX command `sudo`. If your Pi prompts you for a password, the default password is `raspberry`.

You may at this point receive an error telling you that the Pi has failed to fetch certain items. Simply run `sudo reboot` to restart your Pi and then run `sudo apt-get upgrade` again. 

**NOTE**: If your Pi ever fails to download any program or packages, it is usually good practice to `sudo reboot` and then to re-download whatever you were trying to install. This tends to fix the problem a majority of the time.

The problem with `sudo apt-get update` is that it saves the packages to your system regardless of whether you have enough space or not. Remember, your Pi is nowhere nearly as powerful as a laptop or desktop computer, nor does it have the same storage capacity. Everything is run on your Micro SD card (usually 4 or 8GB). You can always check your disk partition, size, and usage by typing `df -h` (view in GB) or `df -m` (view in MB) into the terminal.

Therefore, you will want to keep your Pi clean and lean. Once your packages have upgraded successfully, run `sudo apt-get clean` to dump your apt-get cache. **Be Aware** that this method dumps any memory from your `apt-get` folder. You may have other downloaded items. So be sure that you are willing to dump this information and that you are not currently trying to install or download anything else using `sudo apt-get install`.
 
## 1.5 Configure the Camera 
To install the camera into your Pi, [follow Raspberry Pi's instructional video](https://www.raspberrypi.org/help/camera-module-setup/). 

**NOTE**: Be careful touching any Pi components. If you have built up static electricity, you can short the electronics and ruin your Pi. The easy solution is to touch a non-coated pure metal to ground yourself. While it is not hugely likely you will short your Pi, especially if you are not directly touching circuit components, it is safe practice to ground yourself. **The choice comes down to this**: you accept full responsibility if you have to replace parts.

To configure your camera, run `sudo raspi-config`. Using your up and down keys, scroll down to `Enable Camera` and hit enter to turn the camera on. This is also a good time to expand your SD card partition. This is optional, but it allows you to use the entire SD card to store your files. If you do not expand your partition, you may run into problems installing programs in the future. To do this, within `raspi config` scroll to `Expand Filesystem` and hit enter to partition the card. See Raspberry Pi's [official documentation](https://www.raspberrypi.org/documentation/configuration/raspi-config.md) for more options on configuring your Pi (for instance, you may want to overclock your Pi to get the most power out of it). 

Now scroll down to the bottom with your down key, hit the right side key, and then hit enter to finish to configuration. Your Pi will now reboot. 

To test if you Pi camera is working, open the terminal again and type `raspistill -v -o test.jpg`. This turns the camera on, captures the image, and saves it with the specified name (i.e. in the above example, it saves it as `test.jpg`). The camera will turn on and **after 5 seconds** will capture an image. This gives you enough time to focus the camera on your subject.

Keep an eye on your working directory in the terminal. Unless you have used the `cd` method to change directories to this point, you should still be in the main directory. you can always type `ls` into the terminal to view a list of the current directory's files. On your desktop, navigate to the main directory with you Downloads, Desktop, Music, Pictures, etc. folders. You will see `test.jpg`. Double click it to view your new photo.

### 1.5.1 Download the OCR Engine
Now that we can take photos, we will download the OCR technology to convert our photos of text to actual text files. We will be using [Tesseract](https://github.com/tesseract-ocr/tesseract), a free open source OCR engine sponsored by Google.

In the terminal type `sudo apt-get install tesseract-ocr`.  This will install Tesseract to your Pi, allowing you to run the program from the terminal.

At this point, we will not attempt to take a photo of a document and convert it to a text file using Tesseract. It is very difficult to center and focus the camera on your paper document without some contraption to help you. We will build a simple holder at the end of this lesson.

If you would like to try it out or you have already built a case for you Pi camera, capture an image using `raspistill -v -o ocr.jpg` and then run `tesseract ocr.jpg ocr.txt` to convert the image to an OCRd text file. **Remember** that when running a command on a file in the terminal, you must to either run that command in the same directory as the file, or specify the path to the file. For example, if I run `raspistill -v -o ocr.jpg` in the `Pictures` directory, but attempt to use Tesseract in the `Desktop` directory, I will have to run `tesseract ~/Pictures/ocr.jpg ocr.txt`. This will convert `ocr.jpg` found in the `Pictures` directory and output the `ocr.txt` file to the `Desktop` directory.

**NOTE**: Converting images to text files using Tesseract takes time since your Pi does not have nearly as much processing power as a laptop or desktop computer.

## 1.6 Configuring Sound and Speech
Next we will want to configure our Pi's sound output, text to speech, and then speech to text software. To begin, let's make sure you have audio working on your Pi. 

The core engine of our audio is [Alsa, Linux's sound system](http://www.alsa-project.org/main/index.php/Main_Page). Run `sudo apt-get install alsa-utils` to either download or update Alsa. 

 **Remember** if you run into any errors downloading, first check your internet connection and then run `sudo reboot` to restart your Pi.

Next, load your sound drivers by running `sudo modprobe snd-bcm2835` (you can make sure the drivers have loaded by running `sudo lsmod | grep 2835`). 

**NOTE**: This tutorial assumes that you want to output sound to your TV using HDMI. If you are instead using headphones or speakers plugged into your Pi, skip the following method to edit the system configuration file.

Now let's make sure your pi can output sound to your TV via the HDMI cable. Open the system configuration file with `sudo nano /boot/config.txt`. We can now edit this file within the terminal. The configuration files is simply a list of commands your Pi uses. You will notice that most of these commands have a hashtag `#` in front of them. The `#` is a commenting convention in the text file. Any line with a `#` in front of it is treated by the computer as a comment for humans to read. This allows programmers to explain code in plain English without the computer reading it. However, it also allows programmers to input actual code into a file but to make it unreadable by the machine. This allows other programmers to choose whether or not they want to use that code. We want to use a line in that code. Search for `hdmi_drive=2` and uncomment that line by removing the `#`. To save `config.txt`, hit `control` and the letter `o` together. Now to exit the configuration file and return to the main terminal view, hit `control` and the letter `x`.

To test audio on your Pi, run `speaker-test -t sine -f 440 -c 2 -s 1` in the terminal. This will output a long beeping sound in the form of a sine wave. To test the speech audio output of your Pi, run `aplay /usr/share/sounds/alsa/Front_Center.wav`. You will hear a voice saying "Front and Center" on your TV. 

**NOTE**: You may experience a 2-3 second delay in sound via HDMI. Unfortunately, this is an issue with the Pi connected via HDMI. A possible workaround is to edit your text file to include a few nonsense words at the beginning.

### 1.6.1 Configure Text to Speech
Now let's install [Espeak, a speech synthesizer](http://espeak.sourceforge.net/) we will use for our text to speech method. In the terminal, run `sudo apt-get install espeak`. Once it has installed, run `espeak "Initialize espeak! Hello, it's me. I was wondering if after all these years you'd like espeak"` to test espeak.

### 1.6.2 Configure Speech to Text
Lastly, we want to install a program to convert our computer-spoken audio file back into a text file. For this tutorial, we will be using [PocketSphinx](http://cmusphinx.sourceforge.net/wiki/) since we can run it on our Pi offline. See [this StackOverflow thread](https://raspberrypi.stackexchange.com/questions/10384/speech-processing-on-the-raspberry-pi/10392) on other great options for your Pi.

We will have to install the Sphinx base in order to get Pocket Sphinx to work. To begin, open the terminal and download both Sphinx `wget http://sourceforge.net/projects/cmusphinx/files/sphinxbase/0.8/sphinxbase-0.8.tar.gz` and then PocketSphinx `wget http://sourceforge.net/projects/cmusphinx/files/pocketsphinx/0.8/pocketsphinx-0.8.tar.gz`.

Now extract Sphinx `tar -zxvf pocketsphinx-0.8.tar.gz` and then PocketSphinx `tar -zxvf sphinxbase-0.8.tar.gz`. Once you have successfully extracted these files, you can remove the two downloads by running ` sudo rm -rf pocketsphinx-0.8.tar.gz` and then `sudo rm -rf sphinxbase-0.8.tar.gz`. 

We need [Bison](https://en.wikipedia.org/wiki/GNU_bison) to compile the Sphinx packages. Install Bison by running `sudo apt-get install bison libasound2-dev` in the terminal. 

Once Bison has successfully installed, change directories to the extracted files. To check what they are called exactly, type `ls` into the terminal to show the contents of your main directory. They should be called `sphinxbase-0.8` and `pocketsphinx-0.8`. 

Let's fully compile Sphinx base first. First `cd sphinxbase-0.8`. Then `./configure --enable-fixed`. Now run `sudo make`. This may take several minutes so be patient. Once that is successful, run `sudo make install`. Allow Sphinx to fully install.

Now change back to the main directory by running `cd ..`. Now let's compile PocketSphinx. First `cd pocketsphinx-0.8`. Now run the same commands as above:
`./configure --enable-fixed`, `sudo make`, and then `sudo make install`.

Sphinx will take a bit of time to compile. Be patient and watch ther terminal for any errors from the compiler.

## 1.7 Run OCR, Convert Text to Speech --> Speech to Text
To begin, navigate to the directory you want to be working in. I worked in my home directory. If you want to create a directory, open the terminal and type `mkdir OCR_Project`. Then navigate to the directory by typing `cd OCR_Project`. When doing anything in this project, **make sure all of your files are contained in this directory.**

Make sure you have something to stabilize your camera module. My cardboard box contraption worked fine. I photographed a paper ethics clearance form I had on my desk.

To take a photo called `ocr.jpg` type `raspistill -v -o ocr.jpg` into the terminal.

**Photograph tips**:
- Make sure you only photograph your document and not anything in the background
- Tesseract will not work if your image file is blurry or contains anything other than the document
- Make sure you have a decent amount of light
- Be patient! I took a dozen photographs before I got a functioning image ot OCR.

Check `ocr.jpg` to make sure it is stable, clear, and contains only your document. Otherwise, Tesseract will fail to produce a text file from the image.

To convert the image to a text file, run `tesseract ocr.jpg ocr.txt` in the terminal.

Check `ocr.txt`. The quality of your OCRd image depends on lighting, stability, and the text itself.

We will be using a `.wav` audio file for this tutorial. To convert `ocr.txt` to an audio file called `ocr.wav`, run `espeak -f ocr.txt --stdout > ocr.wav`.

To play your wav file, type `aplay ocr.wav`.

We will now convert this wav file back into a text file called `conversion.txt` using PocketSphinx.

Pocketsphinx audio to text requires your wav file to be 16000 hertz. We will use the software Sox to convert our file to the correct frequency. In the terminal, run `sudo apt-get install sox`. Once you have installed Sox, type `sox ocr.wav -r 16000 16000.wav` to create a wav file called `16000.wav` from `ocr.wav`.

To play the new frequency wav file, type `aplay 16000.wav`.

We will now convert `16000.wav` to a text file called `conversion.txt`. In the terminal, run `pocketsphinx_continuous -infile 16000.wav`. This will run speech recognition on our wav file in the command line. It may take 5-10 minutes so sit back! 

Towards the end of the terminal process, PocketSphinx will output a body of text. This is the converted text from `16000.wav`. Copy the output text from the command line. Open the text editor by selecting `Menu > Accessories > Text Editor` and paste the text into the editor. Save this file as `conversion.txt`.

You should now have the original `ocr.txt` and `conversion.txt` in the same directory. We will now compare these two files.

## 1.8 Connect the Breadboard
To connect the breadboard, power off your Pi and place everything on a flat, clear surface. Connect the female end of the breakout ribbon to your Pi's pins. Be careful but give it a bit of force.

Connect the cobbler to your breadboard. Connect the male end of the ribbon from your Pi to the female end of the cobbler in the breadboard. The breadboard is labelled with numbers and letters and postive and negative inputs. Connect the cobbler to the top of the breadboard. The right most pins should be inserted into `F`.  

Use the following image from Adafruit to connect the remaining components. The script in [section 1.9](19-compare-text-files) will only work if the Green LED is connected to `18` on the cobbler and the Red LED is connected to `23` on the cobbler. 

**NOTE**: The negative leg of the LED is always the shortest! It must be connected to the negative input (the blue line on the furthest side.

![enter image description here](https://learn.adafruit.com/system/assets/assets/000/024/094/original/raspberry_pi_email_blinkies_bb.png?1427489683)

## 1.9 Compare Text Files
We will be using a python script to compare our two text files and visually show us the ratio of similarity between the original file and the translated file. Open the Pi text editor and paste in the following code:

    from difflib import SequenceMatcher
    
    import RPi.GPIO as GPIO

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GREEN_LED = 18
    RED_LED = 23
    GPIO.setup(GREEN_LED, GPIO.OUT)
    GPIO.setup(RED_LED, GPIO.OUT)

    text1 = 'ocr.txt'
    text2 = 'conversion.txt'
    m = SequenceMatcher(None, text1, text2)
    print m.ratio()*100
    
    weight = m.ratio()*100
    
    if weight > 70:
          GPIO.output(GREEN_LED, True)
          GPIO.output(RED_LED, False)
      else:
          GPIO.output(GREEN_LED, False)
          GPIO.output(RED_LED, True)

**NOTE**: Python reads each line's indentation. Make sure you have retained the structure of the above code.

Save the file as `ocr.py` in **the same directory as your two text files.** This code compares `ocr.txt` and `conversion.txt`. If they are 70% or more similar, flash the green LED light on the breadboard. But if they are less than 70% similar, flash the red LED light on the breadboard. If you want to use a different ratio of similarity, go to line 19 and change the `70` in `if weight > 70`.

Now with all the files in the same directory, in the terminal run `sudo python ocr.py`. Depending on the ratio of your texts, you will see a green or red light. 

You will notice that the LED has stayed on. To turn off your LED, we will create another python script called `off.py`

    import RPi.GPIO as GPIO
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GREEN_LED = 18
    RED_LED = 23
    GPIO.setup(GREEN_LED, GPIO.OUT)
    GPIO.setup(RED_LED, GPIO.OUT)
    GPIO.output(GREEN_LED, False)
    GPIO.output(RED_LED, False)

Now run `sudo python off.py` to turn off the LED.

Done!

[![Streamable](http://img.streamable.com/e/2ohc)](https://streamable.com/e/2ohc)

## 1.10 Takeaways
When I began the process of translating my original text, I imagined the text to speech software would fail because of bad OCR. I was surprised. Tesseract OCRd my paper beautifully with few errors. The text to speech operation produced an equally sound audio file with a near perfect reading of the OCRd text file and the original paper. However, when the audio was converted back into a text file, the result was a garbled mess of text.