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
import ssd1306

pin_reset = 16
pin_scl = 15
pin_sda = 4

# reset the oled set it to 1
reset = machine.Pin(pin_reset, machine.Pin.OUT)
reset.value(1);

# setup i2c interface
i2c = machine.I2C(scl=machine.Pin(pin_scl), sda=machine.Pin(pin_sda))

# setup old display to i2c interface
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# clear the display
oled.fill(0)

# write text to the display
oled.text(" Tester V1.0.0", 0, 0)
oled.text("   Created BY", 0, 20)
oled.text("  Jason Peixoto", 0, 30)
oled.text("iotecosystem.com", 0, 50)

# now show the display
oled.show()
