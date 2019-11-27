# Python Serial Translator

Kramer E2000 Serial Translator Raspberry PI as RS232 Gateway

The aim for this project was to connect 2 devices via Serial RS232 even if they speak different dialects. 
2 Years ago, I was called for help because a college of mine failed of connecting 

-	Kramer VS-66HN 6x6 HDMI
To a 
-	KNX RS232 Gateway

I read the Documentation and it turned out that one only talks ASCI and the other only HEX encoded strings. So I wrote this short script and used a Raspberry PI  with 2 RS232 – USB converters to translate between both devices.

Documentation:
Kramer E2000 Protocol 


Raspberry PI Config:

1.	sudo raspi-config 
2.	Select “Boot Options” then “Desktop/CLI” then “Console Autologin” 
3.	Safe & exit
4.	wget https://bitbucket.org/[URlto my script].py 
5.	sudo nano /etc/profile 
6.	sudo python /home/pi/rs232.py & 
7.	Safe & exit
8.	sudo reboot 

