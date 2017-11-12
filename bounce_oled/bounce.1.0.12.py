# IoT Esp8266 Using MicroPython http://micropython.org/
# IOT EcoSystem (c) is copyrighted by Jason Peixoto
# http://www.iotecosystem.com
# Jason Peixoto
# GNU GENERAL PUBLIC LICENSE 3
import utime
import bounce_config
import bounce_oled
import bounce_random

# version
bounce_title = "Bouncer V1.0.12"

# main function
def main():

    bounce_oled.connect_oled(bounce_config.oled_scl, bounce_config.oled_sda, bounce_config.oled_width, bounce_config.oled_height)
    bounce_oled.splash_oled(bounce_title)
    bounce_oled.clear_oled()

    x = y = 0
    dx = bounce_random.random_dx()
    dy = bounce_random.random_dy()

    while True:

        # delete old line
        bounce_oled.drawLine(x, y, x + dx, y + dy, 0)

        # update the dot's position
        x += dx
        y += dy

        # make the dot bounce off the edges of the screen
        if x <= 0: dx = bounce_random.random_dx()

        if x >= (bounce_config.oled_width - 1): dx = - bounce_random.random_dx()

        if y <= 0: dy = bounce_random.random_dy()

        if y >= (bounce_config.oled_height - 1): dy = - bounce_random.random_dy()

        print ("dx " + str(dx) + ":dy " + str(dy) + ":x " + str(x) + ":y " + str(y))

        # draw the line
        bounce_oled.drawLine(x, y, x + dx, y + dy, 1)

        # show the line on the display
        bounce_oled.oled_show()

        # pause for 10 millseconds
        utime.sleep_ms(10)

main()
