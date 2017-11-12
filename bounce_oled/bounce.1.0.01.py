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
import webrepl

# version
bounce_title = " Bouncer V1.0.1"

# start the webrepl
webrepl.start()

# setup i2c interface
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))

# setup old display to i2c interface
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# clear the display
oled.fill(0)

# write text to the display
oled.text(bounce_title, 0, 0)
oled.text("   Created BY", 0, 20)
oled.text("  Jason Peixoto", 0, 30)
oled.text("iotecosystem.com", 0, 50)

# now show the display
oled.show()
