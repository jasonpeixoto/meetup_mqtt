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

i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5), freq=100000)
i2c.start()

chip_id = i2c.readfrom_mem(119, 0xD0, 2)
print(chip_id)
