#!/usr/bin/env python
import time
import serial
# Try to connect to both serial Ports.

try:
     #Serial in and Serial Out does not realy matter this communication work in both directions.
     #ttyUSB0 and USB1 are the default Unix adresses for USBtoSERIAL Adapters. The Onboard RS232 Port is called ttyAMA0
    serialin = serial.Serial(port='/dev/ttyUSB0',baudrate = 9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
    serialout = serial.Serial(port='/dev/ttyUSB1',baudrate = 9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1) 
except:
     #Throw the exaction. if one addapter is missing
     print('Serial Adapter Fehlt, Verbindung fehlgeschlagen')

#Continiouse Cycle loop
while True:
     xinput=serialin.readline()
     xoutput=serialout.readline()
     #Check for pattern
 
     if xinput == "23415620313E312C313E320D0A".decode("hex") or xoutput == "23415620313E312C313E320D0A".decode("hex"):
          #Consolen Output
          print("01818181".decode("hex"))
          time.sleep(0.5)
          print("01818281".decode("hex"))
          #RS232 Output
          serialin.write("01818181".decode("hex"))
          serialout.write("01818181".decode("hex"))
          time.sleep(0.5)
          serialin.write("01818281".decode("hex"))
          serialout.write("01818281".decode("hex"))
     
     if xinput == "23415620323E312C323E320D0A".decode("hex") or xoutput == "23415620323E312C323E320D0A".decode("hex"):
          #Consolen Output
          print("01828181".decode("hex"))
          time.sleep(0.5)
          print("01828281".decode("hex"))
          #RS232 Output
          serialin.write("01828181".decode("hex"))
          serialout.write("01828181".decode("hex"))
          time.sleep(0.5)
          serialin.write("01828281".decode("hex"))
          serialout.write("01828281".decode("hex"))     

     if xinput == "23415620363E312C363E320D0A".decode("hex") or xoutput == "23415620363E312C363E320D0A".decode("hex"):
          #Consolen Output
          print("01868181".decode("hex"))
          time.sleep(0.5)
          print("01868281".decode("hex"))
          #RS232 Output
          serialin.write("01868181".decode("hex"))
          serialout.write("01868181".decode("hex"))
          time.sleep(0.5)
          serialin.write("01868281".decode("hex"))
          serialout.write("01868281".decode("hex"))        

     
     if xinput == "23415620343E332C343E340D0A".decode("hex") or xoutput == "23415620343E332C343E340D0A".decode("hex"):
          #Consolen Output
          print("01848381".decode("hex"))
          time.sleep(0.5)
          print("01848481".decode("hex"))
          #RS232 Output
          serialin.write("01848381".decode("hex"))
          serialout.write("01848381".decode("hex"))
          time.sleep(0.5)
          serialin.write("01848481".decode("hex"))
          serialout.write("01848481".decode("hex"))
      
      
     if xinput == "23415620333E332C333E340D0A".decode("hex") or xoutput == "23415620333E332C333E340D0A".decode("hex"):
          #Consolen Output
          print("01838381".decode("hex"))
          time.sleep(0.5)
          print("01838481".decode("hex"))
          #RS232 Output
          serialin.write("01838381".decode("hex"))
          serialout.write("01838381".decode("hex"))
          time.sleep(0.5)
          serialin.write("01838481".decode("hex"))
          serialout.write("01838481".decode("hex"))     
      
     if xinput == "23415620363E332C363E340D0A".decode("hex") or xoutput == "23415620363E332C363E340D0A".decode("hex"):
          #Consolen Output
          print("01868381".decode("hex"))
          time.sleep(0.5)
          print("01868481".decode("hex"))
          #RS232 Output
          serialin.write("01868381".decode("hex"))
          serialout.write("01868381".decode("hex"))
          time.sleep(0.5)
          serialin.write("01868481".decode("hex"))
          serialout.write("01868481".decode("hex"))  

