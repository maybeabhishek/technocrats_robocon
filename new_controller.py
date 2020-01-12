from __future__ import print_function
import time
import paho.mqtt.client as mqtt
from inputs import get_gamepad
from serial import Serial


def on_connect(client, userdata, flags, rc):
   print("Connected with result code " + str(rc))

   client.subscribe("/leds/pi")


client = mqtt.Client()
client.on_connect = on_connect
client.connect('localhost', 1883, 60)

client.loop_start()

print('Script is running, press Ctrl-C to quit...')
mess = ''
# ser=Serial('/dev/ttyUSB0',9600)
allstates = {'SELECT': 0, 'START': 0, 'WEST': 0, 'SOUTH': 0, 'NORTH': 0, 'EAST': 0, 'DPAD_UP': 0, 'DPAD_DOWN': 0,
    'DPAD_RIGHT': 0, 'DPAD_LEFT': 0, 'THUMBR': 0, 'THUMBL': 0, 'TR': 0, 'TL': 0, 'RX': 0, 'RY': 0, 'RZ': 0, 'X': 0, 'Y': 0, 'Z': 0}

while True:
    events = get_gamepad()
    for event in events:
        btn = event.code
        state = event.state
        if(btn[4:] == 'X' or btn[4:] == 'Y' or btn[4:] == 'RX' or btn[4:] == 'RY'):
            if(abs(state-allstates[btn[4:]]) > 10):
                allstates[btn[4:]] = state
                print(allstates)
        elif(btn != 'SYN_REPORT' and btn != 'MSC_SCAN'):
            allstates[btn[4:]] = state
            # print(allstates)
        if(state == 1):
            dir = btn[4:]
            if(dir=='DPAD_UP'):
                mess='0'
                client.publish('/leds/esp8266', mess)
            elif(dir=='DPAD_DOWN'):
                mess='4'
                client.publish('/leds/esp8266', mess)
            elif(dir=='DPAD_LEFT'):
                mess='6'
                client.publish('/leds/esp8266', mess)
            elif(dir=='DPAD_RIGHT'):
                mess='2'
                client.publish('/leds/esp8266', mess)
            elif(dir=='TL'):
                mess='7'
                client.publish('/leds/esp8266', mess)
            elif(dir=='TR'):
                mess='1'
                client.publish('/leds/esp8266', mess)
            elif(dir=='SELECT'):
                mess='5'
                client.publish('/leds/esp8266', mess)
            elif(dir=='START'):
                mess='3'
                client.publish('/leds/esp8266', mess)

            # forward
            elif(dir=='X' and allstates['X']>4000):
                    if(allstates['X']<20000):
                        mess='<'
                        client.publish('/leds/esp8266', mess)
                        
                    if(allstates['X']>=20000 or allstates['X']<35000 ):
                        mess='>'
                        client.publish('/leds/esp8266', mess)
                        
                    if(allstates['X']>=35000 or allstates['X']<50000 ):
                        mess='('
                        client.publish('/leds/esp8266', mess)
                        
                    if(allstates['X']>=50000):
                        mess=')'
                        client.publish('/leds/esp8266', mess)
                    mess='0'
                    client.publish('/leds/esp8266', mess)
            
            # // back
            elif(dir=='X' and allstates['X']<-4000):
                    if(allstates['X']>-20000):
                        mess='<'
                        client.publish('/leds/esp8266', mess)
                        
                    if(allstates['X']<=-20000 or allstates['X']>-35000 ):
                        mess='>'
                        client.publish('/leds/esp8266', mess)
                        
                    if(allstates['X']<=-35000 or allstates['X']>-50000 ):
                        mess='('
                        client.publish('/leds/esp8266', mess)
                        
                    if(allstates['X']<=-50000):
                        mess=')'
                        client.publish('/leds/esp8266', mess)

                    mess='4'
                    client.publish('/leds/esp8266', mess)

            # // Left
            elif(dir=='RY' and allstates['RY']>4000):
                    if(allstates['RY']<20000):
                        mess='<'
                        client.publish('/leds/esp8266', mess)
                       
                    if(allstates['RY']>=20000 or allstates['RY']<35000 ):
                        mess='>'
                        client.publish('/leds/esp8266', mess)
                        
                    if(allstates['RY']>=35000 or allstates['RY']<50000 ):
                        mess='('
                        client.publish('/leds/esp8266', mess)
                        
                    if(allstates['RY']>=50000):
                        mess=')'
                        client.publish('/leds/esp8266', mess)
                    
                    mess='6'
                    client.publish('/leds/esp8266', mess)
            
            # // Right
            elif(dir=='Y' and allstates['Y']<-4000):
                    if(allstates['Y']>-20000):
                        mess='<'
                        client.publish('/leds/esp8266', mess)
                        
                    if(allstates['Y']<=-20000 or allstates['Y']>-35000 ):
                        mess='>'
                        client.publish('/leds/esp8266', mess)
                        
                    if(allstates['Y']<=-35000 or allstates['Y']>-50000 ):
                        mess='('
                        client.publish('/leds/esp8266', mess)
                        
                    if(allstates['Y']<=-50000):
                        mess=')'
                        client.publish('/leds/esp8266', mess)
                    
                    mess='4'
                    client.publish('/leds/esp8266', mess)
                
        elif(btn[4:]=='REPORT' and btn[4:]!='SCAN'):
                mess='S'
                print(mess)
                client.publish('/leds/esp8266', mess)
        # ser.write(mess.encode('ascii'))
                # print("from b because",btn)
            # print(event.code, event.state)#event.ev_type,
