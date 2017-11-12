# IoT Esp8266 Using MicroPython http://micropython.org/
# Jason Peixoto
# http://www.iotecosystem.com
# IOT EcoSystem (c) is copyrighted by Jason Peixoto
# GNU GENERAL PUBLIC LICENSE 3
#
# Unless required by applicable law or agreed to in writing, this software is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
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

