# IoT Esp8266 by Jason Peixoto 
# IOT EcoSystem (c) 
# www.iotecosystem.com
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

