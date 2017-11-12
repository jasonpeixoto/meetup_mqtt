# IoT Esp8266 Using MicroPython http://micropython.org/
# IOT EcoSystem (c) is copyrighted by Jason Peixoto 
# http://www.iotecosystem.com
# Jason Peixoto 
# GNU GENERAL PUBLIC LICENSE 3
# This file is executed on every boot (including wake-boot from deepsleep)
import gc
import webrepl
webrepl.start()
gc.collect()
