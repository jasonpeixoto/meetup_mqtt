# IoT Esp8266 Using MicroPython http://micropython.org/
# Jason Peixoto
# http://www.iotecosystem.com
# IOT EcoSystem (c) is copyrighted by Jason Peixoto
# GNU GENERAL PUBLIC LICENSE 3
#
# Unless required by applicable law or agreed to in writing, this software is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
import meetup_config
import iot_wifi
import iot_mqtt
import iot_io
import utime
import machine


def sub_callback(topic, msg):
    led.value(int(msg))


led_pin = iot_io.D1  # d1
led = machine.Pin(led_pin, machine.Pin.OUT)

iot_wifi.connect_wifi(meetup_config.wifi_ssid, meetup_config.wifi_password)
iot_wifi.wlan.ifconfig()

client = iot_mqtt.MQTTClient(client_id=meetup_config.mqtt_client, server=meetup_config.mqtt_server)
client.set_callback(sub_callback)
client.connect()
utime.sleep_ms(2000)

client.subscribe(meetup_config.mqtt_base_topic)
utime.sleep_ms(2000)

while True:
    client.check_msg()
    utime.sleep_ms(100)

client.disconnect()