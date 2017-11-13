# IoT Esp8266 Using MicroPython http://micropython.org/
# Jason Peixoto
# http://www.iotecosystem.com
# IOT EcoSystem (c) is copyrighted by Jason Peixoto
# GNU GENERAL PUBLIC LICENSE 3
#
# Unless required by applicable law or agreed to in writing, this software is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
import utime
import bounce_config
import iot_oled
import iot_random

# version
bounce_title = " Bouncer V1.0.7"

# main function
def main():

    iot_oled.connect_oled(bounce_config.oled_scl, bounce_config.oled_sda, bounce_config.oled_width, bounce_config.oled_height)
    iot_oled.splash_oled(bounce_title)
    iot_oled.clear_oled()

    x = y = 0
    dx = dy = 1

    while True:
        # clear old pixel before new pixel
        iot_oled.oled.pixel(x, y, 0)

        # update the dot's position
        x += dx
        y += dy

        # make the dot bounce off the edges of the screen
        if x <= 0: dx = iot_random.random_max(bounce_config.max_dxdy)

        if x >= (bounce_config.oled_width - 1): dx = - iot_random.random_max(bounce_config.max_dxdy)

        if y <= 0: dy = iot_random.random_max(bounce_config.max_dxdy)

        if y >= (bounce_config.oled_height - 1): dy = - iot_random.random_max(bounce_config.max_dxdy)

        print ("dx " + str(dx) + ":dy " + str(dy) + ":x " + str(x) + ":y " + str(y))

        # draw the dot
        iot_oled.oled.pixel(x, y, 1)

        # show the dot on the display
        iot_oled.oled_show()

        # pause for 10 millseconds
        utime.sleep_ms(10)

main()
