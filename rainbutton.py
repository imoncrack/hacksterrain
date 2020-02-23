from twython import Twython
from time import sleep
from gpiozero import LED, Buzzer, InputDevice, Button
import RPi.GPIO as GPIO
import sys
import Adafruit_DHT
from signal import pause
import mysql.connector


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.OUT)
no_rain = InputDevice(18)

bz = Buzzer(19)

n = True

led = LED(23)
ledg = LED(24)
button = Button(13, pull_up=False)

def ledON():
  led.on()
  print("LED is on")
  bz.on()
  print("Buzzer is sounding")

def ledOFF():
  bz.off()
  print("Buzzer has stop sounding")
  led.off()
  print("LED is off")
  ledg.on()
  

n = True

while n == True:
 if not no_rain.is_active:
  print("It's raining, get your clothes out.")
  ledON()
  humidity, temperature = Adafruit_DHT.read_retry(11, 17)
  print('Temp: {:.1f} C'.format(temperature))
  print('Humidity: {:.1f}'.format(humidity))
  n = False
  

button.when_pressed = ledOFF
                   

  	
 	
pause()



	
	