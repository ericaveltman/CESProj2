from pythonosc import osc_message_builder
from pythonosc import udp_client
import serial
import sys
import time

#select the correct port and baud rate 
ser = serial.Serial('/dev/ttyUSB0', 9600)
values = [1] * 4  #mapping = blue button, red button, switch, joystick
valuesOld = ["1"] * 2
bytenum = 0

while True:
    #try:
        
        ser_bytes = ser.readline()
        values[bytenum] = str(ser_bytes, 'ascii').strip()

        if(valuesOld[0] == "0" and values[0] == "1"):
            valuesOld[0] = "1"
        elif(valuesOld[1] == "0" and values[1] == "1"):
            valuesOld[1] = "1"

        if(valuesOld[0] == "1" and values[0] == "0"):
            valuesOld[0] = "0"
        else:
            values[0] = "1"

        if(valuesOld[1] == "1" and values[1] == "0"):
            valuesOld[1] = "0"
        else:
            values[1] = "1"
        

        bytenum += 1
        if bytenum == 4:
            bytenum %= 4

        #print(values)
        joystickVal = (int(values[3]) - 0) / (4095 - 0) * (12 - (-12)) + (-12)   #(x - input_start) / (input_end - input_start) * (output_end - output_start) + output_start
        #print(joystickVal)

        if((values[0] == "0" or values[1] == "0") and values[2] == "0" and (joystickVal < 0.5 and joystickVal > -0.5)):   #play regular note
        
            if(values[0] == "0"):                        #play note
                sender = udp_client.SimpleUDPClient('127.0.0.1', 4560)
                sender.send_message('/trigger/blade', [70, 100, 1])
                time.sleep(2)

            elif(values[1] == "0"):
                sender = udp_client.SimpleUDPClient('127.0.0.1', 4560)
                sender.send_message('/trigger/piano', [70, 100, 1])
                time.sleep(2)

        elif((values[0] == "0" or values[1] == "0") and values[2] == "1" and (joystickVal < 0.5 and joystickVal > -0.5)):   #play note w/ reverb

            if(values[0] == "0"):                          
                sender = udp_client.SimpleUDPClient('127.0.0.1', 4560)
                sender.send_message('/trigger/bladeverb', [70, 100, 1])
                time.sleep(2)

            elif(values[1] == "0"):
                sender = udp_client.SimpleUDPClient('127.0.0.1', 4560)
                sender.send_message('/trigger/pianoverb', [70, 100, 1])
                time.sleep(2)

        elif((values[0] == "0" or values[1] == "0") and values[2] == "0" and (joystickVal >= 0.5 or joystickVal <= -0.5)):   #play note w/ pitchshift
                
            if(values[0] == "0"):
                sender = udp_client.SimpleUDPClient('127.0.0.1', 4560)
                sender.send_message('/trigger/bladepitch', [70, 100, 1, joystickVal])
                time.sleep(2)

            elif(values[1] == "0"):
                sender = udp_client.SimpleUDPClient('127.0.0.1', 4560)
                sender.send_message('/trigger/pianopitch', [70, 100, 1, joystickVal])
                time.sleep(2)
            
        elif((values[0] == "0" or values[1] == "0") and values[2] == "1" and (joystickVal < 0.5 or joystickVal > -0.5)):   #play note w/ all effects
       
            if(values[0] == "0"):                          
                sender = udp_client.SimpleUDPClient('127.0.0.1', 4560)
                sender.send_message('/trigger/bladeall', [70, 100, 1, joystickVal])
                time.sleep(2)

            elif(values[1] == "0"):
                sender = udp_client.SimpleUDPClient('127.0.0.1', 4560)
                sender.send_message('/trigger/pianoall', [70, 100, 1, joystickVal])
                time.sleep(2)

    # except:
    #     print(sys.exc_info()[0])
    #     break