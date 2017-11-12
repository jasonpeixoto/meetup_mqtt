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

button_pin = iot_io.D2       # d1

# create pin for each led
button = machine.Pin(button_pin, machine.Pin.IN)

while True:
    time.sleep_ms(200)
    print(button.value())