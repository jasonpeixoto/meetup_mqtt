# IoT Esp8266 Using MicroPython http://micropython.org/
# IOT EcoSystem (c) is copyrighted by Jason Peixoto 
# http://www.iotecosystem.com
# Jason Peixoto 
# GNU GENERAL PUBLIC LICENSE 3
import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan_list = wlan.scan()

for i in wlan_list:
    print(i)
