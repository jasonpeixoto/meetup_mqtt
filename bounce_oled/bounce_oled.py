# IoT Esp8266 Using MicroPython http://micropython.org/
# IOT EcoSystem (c) is copyrighted by Jason Peixoto
# http://www.iotecosystem.com
# Jason Peixoto
# GNU GENERAL PUBLIC LICENSE 3
import machine
import ssd1306
import utime

# connect to i2c and display setup, pass parameters to setup i2c + ssd1306
def connect_oled(oled_scl, oled_sda, oled_width, oled_height):
    global i2c, oled

    i2c = machine.I2C(scl=machine.Pin(oled_scl), sda=machine.Pin(oled_sda))
    oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


# display the splash display
def splash_oled(title):
    global oled

    oled.fill(0)
    oled.text(title, 0, 0)
    oled.text("   Created BY", 0, 20)
    oled.text("  Jason Peixoto", 0, 30)
    oled.text("iotecosystem.com", 0, 50)
    oled.show()
    utime.sleep_ms(3000)


# clear the display
def clear_oled():
    global oled

    oled.fill(0)
    oled.show()


def oled_show():
    global oled

    oled.show()


# draw line [Bresenham's line algorithm]
def drawLine(x0, y0, x1, y1, fill):
    global oled

    steep = abs(y1 - y0) > abs(x1 - x0);
    if steep:
        x0, y0 = y0, x0
        x1, y1 = y1, x1
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    dx = x1 - x0
    dy = abs(y1 - y0)
    err = dx / 2
    ystep = -1
    if y0 < y1: ystep = 1
    for xx in range(x0, x1):
        if steep:
            oled.pixel(y0, xx, fill)
        else:
            oled.pixel(xx, y0, fill)
        err -= dy
        if err < 0:
            y0 += ystep
            err += dx


# draw a rectagle using 4 lines
def drawRect(x, y, w, h, fill):
    drawLine(x, y, x + w, y, fill)
    drawLine(x + w - 1, y, x + w - 1, y + h, fill)
    drawLine(x + w, y + h - 1, x, y + h - 1, fill)
    drawLine(x, y + h, x, y, fill)

