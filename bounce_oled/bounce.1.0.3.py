# IoT Esp8266 Using MicroPython http://micropython.org/
# IOT EcoSystem (c) is copyrighted by Jason Peixoto
# http://www.iotecosystem.com
# Jason Peixoto
# GNU GENERAL PUBLIC LICENSE 3
import machine
import ssd1306
import utime
import webrepl
import bounce_config

# version
bounce_title = " Bouncer V1.0.3"

# connect to i2c and display setup, pass parameters to setup i2c + ssd1306
def connect_oled(oled_scl, oled_sda, oled_width, oled_height):
    global i2c, oled

    i2c = machine.I2C(scl=machine.Pin(oled_scl), sda=machine.Pin(oled_sda))
    oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


# display the splash display
def splash_oled(title):
    oled.fill(0)
    oled.text(title, 0, 0)
    oled.text("   Created BY", 0, 20)
    oled.text("  Jason Peixoto", 0, 30)
    oled.text("iotecosystem.com", 0, 50)
    oled.show()
    utime.sleep_ms(3000)


# clear the display
def clear_oled():
    oled.fill(0)
    oled.show()


# main function
def main():
    # start the webrepl
    webrepl.start()

    # connect to the oled
    connect_oled(bounce_config.oled_scl, bounce_config.oled_sda, bounce_config.oled_width, bounce_config.oled_height)

    # show splash screen
    splash_oled(bounce_title)

    # clear the screen
    clear_oled()

    while True:


        utime.sleep_ms(1000)  # pause for 1 second

main()
