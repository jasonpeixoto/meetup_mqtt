# IoT Esp8266 Using MicroPython http://micropython.org/
# Jason Peixoto
# http://www.iotecosystem.com
# IOT EcoSystem (c) is copyrighted by Jason Peixoto
# GNU GENERAL PUBLIC LICENSE 3
#
# Unless required by applicable law or agreed to in writing, this software is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
import machine
import time
import iot_io

led_pin = iot_io.D1       # d1

# create pin for each led
led = machine.Pin(led_pin, machine.Pin.OUT)

for i in range(10):
    led.value(0);
    time.sleep(0.5);
    led.value(1);
    time.sleep(0.5);