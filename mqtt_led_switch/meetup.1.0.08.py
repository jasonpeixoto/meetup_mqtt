# IoT Esp8266 Using MicroPython http://micropython.org/
# Jason Peixoto
# http://www.iotecosystem.com
# IOT EcoSystem (c) is copyrighted by Jason Peixoto
# GNU GENERAL PUBLIC LICENSE 3
#
# Unless required by applicable law or agreed to in writing, this software is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
import iot_config
import iot_wifi
import iot_mqtt
import utime

iot_wifi.connect_wifi(iot_config.wifi_ssid, iot_config.wifi_password)
iot_wifi.wlan.ifconfig()

#client = iot_mqtt.MQTTClient(client_id=iot_config.mqtt_client, server=iot_config.mqtt_server, port=1883, user=iot_config.mqtt_username, password=iot_config.mqtt_password)
client = iot_mqtt.MQTTClient(client_id=iot_config.mqtt_client, server=iot_config.mqtt_server)

client.connect()
utime.sleep_ms(2000)

client.publish(iot_config.mqtt_base_topic, "hello World")
utime.sleep_ms(500)

client.disconnect()
