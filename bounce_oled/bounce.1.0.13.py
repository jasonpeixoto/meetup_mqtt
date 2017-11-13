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
bounce_title = "Bouncer V1.0.13"

# define box to operate in
min_x = 0
max_x = bounce_config.oled_width-1
min_y = 0
max_y = bounce_config.oled_height-1

# main function
def main():

    iot_oled.connect_oled(bounce_config.oled_scl, bounce_config.oled_sda, bounce_config.oled_width, bounce_config.oled_height)
    iot_oled.splash_oled(bounce_title)
    iot_oled.clear_oled()

    x = min_x
    y = min_y
    dx = iot_random.random_dx()
    dy = iot_random.random_dy()

    while True:

        # delete old line
        iot_oled.drawLine(x, y, x + dx, y + dy, 0)

        # update the dot's position
        x += dx
        y += dy

        # make the dot bounce off the edges of the screen
        if x < min_x:
            dx = iot_random.random_dx()
            x = min_x

        if x > max_x:
            dx = - iot_random.random_dx()
            x = max_x

        if y < min_y:
            dy = iot_random.random_dy()
            y = min_y

        if y > max_y:
            dy = - iot_random.random_dy()
            y = max_y

        print ("dx " + str(dx) + ":dy " + str(dy) + ":x " + str(x) + ":y " + str(y))

        # draw the line
        iot_oled.drawLine(x, y, x + dx, y + dy, 1)

        # show the line on the display
        iot_oled.oled_show()

        # pause for 10 millseconds
        utime.sleep_ms(10)

main()
