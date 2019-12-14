import time 
import RPi.GPIO as GPIO 
import paho.mqtt.client as mqtt 
from __future__ import print_function
from inputs import get_gamepad
from serial import Serial

# Configuration: 
LED_PIN        = 24 
BUTTON_PIN     = 23 
# Initialize GPIO for LED and button. 
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False) 
GPIO.setup(LED_PIN, GPIO.OUT) 
GPIO.output(LED_PIN, GPIO.LOW) 
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP) 



def on_connect(client, userdata, flags, rc): 
   print("Connected with result code " + str(rc)) 
   
   client.subscribe("/leds/pi") 
 



def on_message(client, userdata, msg): 
   print(msg.topic+" "+str( msg.payload)) 

   if msg.topic == '/leds/pi': 
       
       if msg.payload == b'ON': 
           GPIO.output(LED_PIN, GPIO.HIGH) 
       elif msg.payload == b'OFF': 
           GPIO.output(LED_PIN, GPIO.LOW) 
       elif msg.payload == b'TOGGLE': 
           GPIO.output(LED_PIN, not GPIO.input(LED_PIN)) 


client = mqtt.Client() 
client.on_connect = on_connect 
client.on_message = on_message 
client.connect('localhost', 1883, 60) 

client.loop_start() 

print('Script is running, press Ctrl-C to quit...') 
mess=''
#ser=Serial('/dev/ttyUSB0',9600)
allstates={'SELECT':0,'START':0,'WEST':0,'SOUTH':0,'NORTH':0,'EAST':0,'DPAD_UP':0,'DPAD_DOWN':0,'DPAD_RIGHT':0,'DPAD_LEFT':0,'THUMBR':0,'THUMBL':0,'TR':0,'TL':0,'RX':0,'RY':0,'RZ':0,'X':0,'Y':0,'Z':0}

while True:
    events = get_gamepad()
    for event in events:
        btn=event.code
        state=event.state
        if(btn[4:]=='X' or btn[4:]=='Y' or btn[4:]=='RX' or btn[4:]=='RY'):
            if(abs(state-allstates[btn[4:]])>10):
                allstates[btn[4:]]=state
                print(allstates)
        elif(btn!='SYN_REPORT' and btn!='MSC_SCAN'):
            allstates[btn[4:]]=state
            #print(allstates)
        if(state==1):
            dir=btn[4:]
            if(dir=='DPAD_UP'):
                mess='0000000000000000000000000000'
                client.publish('/leds/esp8266', mess)
            elif(dir=='DPAD_DOWN'):
                mess='4444444444444444444444444444'
                client.publish('/leds/esp8266', mess)
            elif(dir=='DPAD_LEFT'):
                mess='6666666666666666666666666666'
                client.publish('/leds/esp8266', mess)
            elif(dir=='DPAD_RIGHT'):
                mess='2222222222222222222222222222'
                client.publish('/leds/esp8266', mess)
            elif(dir=='TL'):
                mess='77777777777777777777777777777'
                client.publish('/leds/esp8266', mess)
            elif(dir=='TR'):
                mess='111111111111111111111111111111'
                client.publish('/leds/esp8266', mess)
            elif(dir=='SELECT'):
                mess='555555555555555555555555555555'
                client.publish('/leds/esp8266', mess)
            elif(dir=='START'):
                mess='3333333333333333333333333333333'
                client.publish('/leds/esp8266', mess)
        else:
            mess='S'
            print(mess)
            client.publish('/leds/esp8266', mess)
        # ser.write(mess.encode('ascii'))
                #print("from b because",btn)
            #print(event.code, event.state)#event.ev_type,

