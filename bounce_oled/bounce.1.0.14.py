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
bounce_title = "Bouncer V1.0.14"

# define box to operate in
min_x = round(bounce_config.oled_width/4)
max_x = (min_x*3)-1
min_y = round(bounce_config.oled_height/4)
max_y = (min_y*3)-1

# main function
def main():

    bounce_oled.connect_oled(bounce_config.oled_scl, bounce_config.oled_sda, bounce_config.oled_width, bounce_config.oled_height)
    bounce_oled.splash_oled(bounce_title)
    bounce_oled.clear_oled()

    x = min_x
    y = min_y
    dx = bounce_random.random_dx()
    dy = bounce_random.random_dy()

    while True:

        # delete old line
        bounce_oled.drawLine(x, y, x + dx, y + dy, 0)

        # update the dot's position
        x += dx
        y += dy

        # make the dot bounce off the edges of the screen
        if x < min_x:
            dx = bounce_random.random_dx()
            x = min_x

        if x > max_x:
            dx = - bounce_random.random_dx()
            x = max_x

        if y < min_y:
            dy = bounce_random.random_dy()
            y = min_y

        if y > max_y:
            dy = - bounce_random.random_dy()
            y = max_y

        print ("dx " + str(dx) + ":dy " + str(dy) + ":x " + str(x) + ":y " + str(y))

        # draw the line
        bounce_oled.drawLine(x, y, x + dx, y + dy, 1)

        # show the line on the display
        bounce_oled.oled_show()

        # pause for 10 millseconds
        utime.sleep_ms(10)

main()
