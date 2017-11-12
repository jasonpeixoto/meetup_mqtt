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
import bounce_oled
import bounce_random

# version
bounce_title = " Bouncer V1.0.9"

# config for our bouncer
max_loop = 20
index_loop = 0


# update index to show max lines at any time.
def update_oled_loop():
    global index_loop, max_loop

    index_loop = index_loop + 1
    if(index_loop >= max_loop):
        bounce_oled.clear_oled()
        index_loop = 0


# main function
def main():

    bounce_oled.connect_oled(bounce_config.oled_scl, bounce_config.oled_sda, bounce_config.oled_width, bounce_config.oled_height)
    bounce_oled.splash_oled(bounce_title)
    bounce_oled.clear_oled()

    x = y = 0
    dx = bounce_random.random_dxdy()
    dy = bounce_random.random_dxdy()

    while True:
        # update the dot's position
        x += dx
        y += dy

        # make the dot bounce off the edges of the screen
        if x <= 0:
            dx = bounce_random.random_dxdy()
            update_oled_loop()

        if x >= (bounce_config.oled_width - 1):
            dx = - bounce_random.random_dxdy()
            update_oled_loop()

        if y <= 0:
            dy = bounce_random.random_dxdy()
            update_oled_loop()

        if y >= (bounce_config.oled_height - 1):
            dy = - bounce_random.random_dxdy()
            update_oled_loop()

        print ("dx " + str(dx) + ":dy " + str(dy) + ":x " + str(x) + ":y " + str(y))

        # draw the dot
        bounce_oled.oled.pixel(x, y, 1)

        # show the dot on the display
        bounce_oled.oled_show()

        # pause for 10 millseconds
        utime.sleep_ms(10)

main()
