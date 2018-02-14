# MailReader

Deployment process :

1. Installing python 2.7 version on raspbian OS on raspberry pi.

2. Install python package manager pip.
	sudo apt-get install python-pip python-dev build-essential

3. Install python imaplib, getpass and email library.
	sudo pip install <library name>

4. Installing and configuring audio on pi, follow instructions on:
	http://iwearshorts.com/blog/raspberry-pi-setting-up-your-audio/

5.For text to speech output: follow instructions on
	http://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Install_supporting_packages
	http://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Espeak_Text_to_Speech

6.Install GrovePi for lcd output. Clone github repo, and follow installing instructions on it.
	https://github.com/DexterInd/GrovePi

7. Finally run following command in this folder containing google.sh:
	chmod +x google.sh
	python mailReceiver.py
  
  
  Connecting  circuit :

How to connect LCD to Pi :
	> connect “GND” pin of LCD (shown in diagram) to “GND” pin ( like pin 6 ) of Raspberry Pi.
	> connect “VCC” pin of LCD (shown in diagram) to “5 V PWR” pin ( like pin 2,4 ) of Raspberry Pi.
	> connect “SDA” pin of LCD (shown in diagram) to “I2C1 SDA” pin ( pin 3 ) of Raspberry Pi.
	> connect “SCL” pin of LCD (shown in diagram) to “I2C1 SCL” pin ( pin 5 ) of Raspberry Pi.
