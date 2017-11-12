# IoT Esp8266 Using MicroPython http://micropython.org/
# IOT EcoSystem (c) is copyrighted by Jason Peixoto
# http://www.iotecosystem.com
# Jason Peixoto
# GNU GENERAL PUBLIC LICENSE 3
import utime
import bounce_config
import bounce_oled

# version
bounce_title = " Bouncer V1.0.5"

# main function
def main():

    bounce_oled.connect_oled(bounce_config.oled_scl, bounce_config.oled_sda, bounce_config.oled_width, bounce_config.oled_height)
    bounce_oled.splash_oled(bounce_title)
    bounce_oled.clear_oled()

    x = y = 0
    dx = dy = 1

    while True:
        # clear old pixel before new pixel
        bounce_oled.oled.pixel(x, y, 0)

        # update the dot's position
        x += dx
        y += dy

        # make the dot bounce off the edges of the screen for both X and Y
        if (x <= 0) or (x >= (bounce_config.oled_width - 1)): dx = -dx
        if (y <= 0) or (y >= (bounce_config.oled_height - 1)): dy = -dy

        print ("dx " + str(dx) + ":dy " + str(dy) + ":x " + str(x) + ":y " + str(y))

        # draw the dot
        bounce_oled.oled.pixel(x, y, 1)

        # show the dot on the display
        bounce_oled.oled_show()

        # pause for 10 millseconds
        utime.sleep_ms(10)

main()
