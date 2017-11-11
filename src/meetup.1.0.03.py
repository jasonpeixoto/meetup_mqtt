import network

wifi_ssid = "Park&B 1"
wifi_password = "bluewater19%"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(wifi_ssid, wifi_password)
wlan.ifconfig()
