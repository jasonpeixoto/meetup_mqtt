# IoT Esp8266 Using MicroPython http://micropython.org/
# IOT EcoSystem (c) is copyrighted by Jason Peixoto 
# http://www.iotecosystem.com
# Jason Peixoto 
# GNU GENERAL PUBLIC LICENSE 3
import time

wifi_ssid = "Park&B 1"
wifi_password = "bluewater19%"

mqtt_server = "test.mosquitto.org"
mqtt_client = "jason_" + str(time.time())
mqtt_username = "admin"
mqtt_password = "admin"
mqtt_base_topic = "/abc"
