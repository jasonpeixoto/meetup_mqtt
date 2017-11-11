import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan_list = wlan.scan()

for i in wlan_list:
    print(i)