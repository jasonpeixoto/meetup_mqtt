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

led_pin = iot_io.D1
button_pin = iot_io.D2

led = machine.Pin(led_pin, machine.Pin.OUT)
button = machine.Pin(button_pin, machine.Pin.IN)

while True:
    time.sleep_ms(200)
    led.value(button.value())