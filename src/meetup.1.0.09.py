# IoT Esp8266 Using MicroPython http://micropython.org/
# IOT EcoSystem (c) is copyrighted by Jason Peixoto 
# http://www.iotecosystem.com
# Jason Peixoto 
# GNU GENERAL PUBLIC LICENSE 3
import machine
import iot_io
import iot_config
import iot_wifi
import iot_mqtt
import utime
import time

button_pin = iot_io.D2
button = machine.Pin(button_pin, machine.Pin.IN)

iot_wifi.connect_wifi(iot_config.wifi_ssid, iot_config.wifi_password)
iot_wifi.wlan.ifconfig()

client = iot_mqtt.MQTTClient(client_id=iot_config.mqtt_client, server=iot_config.mqtt_server)

client.connect()
utime.sleep_ms(2000)

last_state = ~button.value()
while True:
    time.sleep_ms(200)
    while True:
        if button.value() != last_state:
            break
        time.sleep_ms(20)
    last_state = button.value();
    client.publish(iot_config.mqtt_base_topic, str(last_state))

#utime.sleep_ms(500)

client.disconnect()
