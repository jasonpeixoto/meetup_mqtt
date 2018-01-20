# IoT Esp8266 Using MicroPython http://micropython.org/
# Jason Peixoto
# http://www.iotecosystem.com
# IOT EcoSystem (c) is copyrighted by Jason Peixoto
# GNU GENERAL PUBLIC LICENSE 3
#
# Unless required by applicable law or agreed to in writing, this software is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
from bmp180 import BMP180
from machine import I2C, Pin

bus =  I2C(scl=Pin(4), sda=Pin(5), freq=100000)
bmp180 = BMP180(bus)
bmp180.oversample_sett = 2
bmp180.baseline = 101325

temp = bmp180.temperature
p = bmp180.pressure
altitude = bmp180.altitude
print(temp, p, altitude)