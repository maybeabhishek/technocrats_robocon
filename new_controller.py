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
client.connect('localhost', 1883, 55)

client.loop_start()

print('Script is running, press Ctrl-C to quit...')
mess = ''
# ser=Serial('/dev/ttyUSB0',9550)
allstates = {'SELECT': 0, 'START': 0, 'WEST': 0, 'SOUTH': 0, 'NORTH': 0, 'EAST': 0, 'DPAD_UP': 0, 'DPAD_DOWN': 0,
    'DPAD_RIGHT': 0, 'DPAD_LEFT': 0, 'THUMBR': 0, 'THUMBL': 0, 'TR': 0, 'TL': 0, 'RX': 0, 'RY': 0, 'RZ': 0, 'X': 0, 'Y': 0, 'Z': 0}

while True:
    events = get_gamepad()
    for event in events:
        btn = event.code
        state = event.state
        dir = btn[4:]
        if(btn[4:] == 'X' or btn[4:] == 'Y' or btn[4:] == 'RX' or btn[4:] == 'RY'):
            if(abs(state-allstates[btn[4:]]) > 10):
                allstates[btn[4:]] = state
                # print(allstates)   # Make it print later
        elif(btn != 'SYN_REPORT' and btn != 'MSC_SCAN'):
            allstates[btn[4:]] = state
            # print(allstates)
        # if(state == 1):
        #     dir = btn[4:]
        #     if(dir=='DPAD_UP'):
        #         mess='0'
        #         client.publish('/leds/esp8266', mess)
        #     elif(dir=='DPAD_DOWN'):
        #         mess='4'
        #         client.publish('/leds/esp8266', mess)
        #     elif(dir=='DPAD_LEFT'):
        #         mess='6'
        #         client.publish('/leds/esp8266', mess)
        #     elif(dir=='DPAD_RIGHT'):
        #         mess='2'
        #         client.publish('/leds/esp8266', mess)
        #     elif(dir=='TL'):
        #         mess='7'
        #         client.publish('/leds/esp8266', mess)
        #     elif(dir=='TR'):
        #         mess='1'
        #         client.publish('/leds/esp8266', mess)
        #     elif(dir=='SELECT'):
        #         mess='5'
        #         client.publish('/leds/esp8266', mess)
        #     elif(dir=='START'):
        #         mess='3'
        #         client.publish('/leds/esp8266', mess)

        # elif(btn[4:]!='REPORT' and btn[4:]=='SCAN'):
        #         mess='S'
        #         print(mess)
        #         client.publish('/leds/esp8266', mess)

            # forward
        if(dir=='Y' and allstates['Y']<105):
            if(allstates['Y']<=105 and allstates['Y']>80):
                mess='<'
                
                client.publish('/leds/esp8266', mess)
                
            elif(allstates['Y']>55 and allstates['Y']<=80 ):
                mess='>'
                client.publish('/leds/esp8266', mess)
                
            elif(allstates['Y']>30 and allstates['Y']<=55 ):
                mess='('
                client.publish('/leds/esp8266', mess)
                
            elif(allstates['Y']<=30):
                mess=')'
                client.publish('/leds/esp8266', mess)
            print(mess)
            mess='0'
            print(mess)
            client.publish('/leds/esp8266', mess)
        
        # left
        elif(dir=='RX' and allstates['RX']<105):
            if(allstates['RX']<=105 and allstates['RX']>80):
                mess='<'
                client.publish('/leds/esp8266', mess)
                
            elif(allstates['RX']>55 and allstates['RX']<=80 ):
                mess='>'
                client.publish('/leds/esp8266', mess)
                
            elif(allstates['RX']>30 and allstates['RX']<=55 ):
                mess='('
                client.publish('/leds/esp8266', mess)
                
            elif(allstates['RX']<=30):
                mess=')'
                client.publish('/leds/esp8266', mess)
            print(mess)
            mess='6'
            print(mess)
            client.publish('/leds/esp8266', mess)
        # back
        elif(dir=='Y' and allstates['Y']>145):
            if(allstates['Y']>=145 and allstates['Y']<=170):
                mess='<'
                client.publish('/leds/esp8266', mess)
                
            elif(allstates['Y']>170 and allstates['Y']<=195 ):
                mess='>'
                client.publish('/leds/esp8266', mess)
                
            elif(allstates['Y']>195 and allstates['Y']<=220 ):
                mess='('
                client.publish('/leds/esp8266', mess)
                
            else:
                mess=')'
                client.publish('/leds/esp8266', mess)
            print(mess)
            mess='4'
            print(mess)
            client.publish('/leds/esp8266', mess)

        # right
        elif(dir=='RX' and allstates['RX']>145):
            if(allstates['RX']>=145 and allstates['RX']<=170):
                mess='<'
                client.publish('/leds/esp8266', mess)
                
            elif(allstates['RX']>170 and allstates['RX']<=195 ):
                mess='>'
                client.publish('/leds/esp8266', mess)
                
            elif(allstates['RX']>195 and allstates['RX']<=220 ):
                mess='('
                client.publish('/leds/esp8266', mess)
                
            else:
                mess=')'
                client.publish('/leds/esp8266', mess)
            print(mess)
            mess='2'
            print(mess)
            client.publish('/leds/esp8266', mess)
               
        elif(allstates['RX']>105 and allstates['RX']<145 and allstates['Y']>105 and allstates['Y']<145 and mess!='S'):
            
            mess='S'
            print(mess)
            client.publish('/leds/esp8266', mess)
        # ser.write(mess.encode('ascii'))
                # print("from b because",btn)
            # print(event.code, event.state)#event.ev_type,
