# IoT Esp8266 Using MicroPython http://micropython.org/
# IOT EcoSystem (c) is copyrighted by Jason Peixoto
# http://www.iotecosystem.com
# Jason Peixoto
# GNU GENERAL PUBLIC LICENSE 3
import urandom
import bounce_config

# get a random number 32 bits = long and return as a float < 1 (2^32 - 1)
def random_float():
   return urandom.getrandbits(32)/4294967295.0


# return as int
def random_int():
   return urandom.getrandbits(32)


# get a random number 0 to max
def random_max(max):
    max = round(max)
    return random_minmax(0, max)


# return random number between min and max
def random_minmax(min, max):
    min = round(min)
    max = round(max)
    return (random_int() % (max-min)) + min;


# return 1 to
def random_dxdy():
    return random_minmax(1*bounce_config.max_dxdy, bounce_config.max_dxdy*bounce_config.max_dxdy)


# return 1 to max_dxdy
def random_dx():
    return random_minmax(1*bounce_config.max_dxdy*2, bounce_config.max_dxdy*bounce_config.max_dxdy*4)


# return 1 to max_dxdy
def random_dy():
    return random_minmax(1*bounce_config.max_dxdy, bounce_config.max_dxdy*bounce_config.max_dxdy)