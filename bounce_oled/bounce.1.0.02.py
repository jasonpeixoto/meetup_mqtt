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
import utime
import webrepl
import bounce_config

# version
bounce_title = " Bouncer V1.0.2"

# start the webrepl
webrepl.start()

# setup i2c interface
i2c = machine.I2C(scl=machine.Pin(bounce_config.oled_scl), sda=machine.Pin(bounce_config.oled_sda))

#setup oled display to i2c interface
oled = ssd1306.SSD1306_I2C(bounce_config.oled_width, bounce_config.oled_height, i2c)

# clear the oled
oled.fill(0)

# display text
oled.text(bounce_title, 0, 0)
oled.text("   Created BY", 0, 20)
oled.text("  Jason Peixoto", 0, 30)
oled.text("iotecosystem.com", 0, 50)

# now show the oled
oled.show()

#delay for 3 secons
utime.sleep_ms(3000)
