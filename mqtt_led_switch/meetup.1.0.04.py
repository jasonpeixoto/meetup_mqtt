# IoT Esp8266 Using MicroPython http://micropython.org/
# IOT EcoSystem (c) is copyrighted by Jason Peixoto 
# http://www.iotecosystem.com
# Jason Peixoto 
# GNU GENERAL PUBLIC LICENSE 3
import iot_config
import iot_wifi

iot_wifi.connect_wifi(iot_config.wifi_ssid, iot_config.wifi_password)
