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
bounce_title = "Bouncer V1.0.16"

# define box to operate in
shift_y = 4
min_x = round(bounce_config.oled_width/5)
max_x = (min_x*4)-1
min_y = round(bounce_config.oled_height/5) + shift_y
max_y = ((min_y-shift_y)*4)-1


# main function
def main():

    iot_oled.connect_oled(bounce_config.oled_scl, bounce_config.oled_sda, bounce_config.oled_width, bounce_config.oled_height)
    iot_oled.splash_oled(bounce_title)
    iot_oled.clear_oled()

    x = min_x + 1
    y = min_y + 1
    dx = iot_random.max_dxdy
    dy = iot_random.max_dxdy

    iot_oled.drawRect(min_x, min_y, max_x - min_x + 1, max_y - min_y + 1, 1)

    while True:

        # delete old line
        iot_oled.drawLine(x, y, x + dx, y + dy, 0)

        # update the dot's position
        x += dx
        y += dy

        # make the dot bounce off the edges of the screen
        if x + dx <= min_x+1:
            x = min_x + 1
            dx = iot_random.random_dxdy()
            if (x + dx >= max_x):
                dx = iot_random.max_dxdy

        if x + dx >= max_x - 1:
            x = max_x - 1
            dx = - iot_random.random_dxdy()
            if (x + dx <= min_x):
                dx = iot_random.max_dxdy

        if y + dy <= min_y + 1:
            y = min_y + 1
            dy = iot_random.random_dxdy()
            if (y + dy >= max_y):
                dy = iot_random.max_dxdy

        if y + dy >= max_y - 1:
            y = max_y - 1
            dy = - iot_random.random_dxdy()
            if (y + dy <= min_y):
                dy = iot_random.max_dxdy

        print ("dx " + str(dx) + ":dy " + str(dy) + ":x " + str(x) + ":y " + str(y))

        # draw the line
        iot_oled.drawLine(x, y, x + dx, y + dy, 1)

        # show the line on the display
        iot_oled.oled.show()

        # pause for 10 millseconds
        utime.sleep_ms(10)

main()
