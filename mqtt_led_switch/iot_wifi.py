# IoT Esp8266 Using MicroPython http://micropython.org/
# IOT EcoSystem (c) is copyrighted by Jason Peixoto 
# http://www.iotecosystem.com
# Jason Peixoto 
# GNU GENERAL PUBLIC LICENSE 3
import network
import utime

# return true if sucess, false of timeout or failed.
def connect_wifi(wifi_ssid, wifi_password):
    global wlan
    try:
        wlan = network.WLAN(network.STA_IF)

        if not wlan.isconnected():
            wlan.active(True)
            wlan.connect(wifi_ssid, wifi_password)
            while not wlan.isconnected():
                utime.sleep_ms(100)
        wlan.ifconfig()
        return wlan.isconnected()
    except:
        return False

