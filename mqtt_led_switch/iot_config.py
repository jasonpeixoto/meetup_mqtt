# IoT Esp8266 Using MicroPython http://micropython.org/
# Jason Peixoto
# http://www.iotecosystem.com
# IOT EcoSystem (c) is copyrighted by Jason Peixoto
# GNU GENERAL PUBLIC LICENSE 3
#
# Unless required by applicable law or agreed to in writing, this software is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
import time

wifi_ssid = "Park&B 1"
wifi_password = "bluewater19%"

mqtt_server = "test.mosquitto.org"
mqtt_client = "jason_" + str(time.time())
mqtt_username = "admin"
mqtt_password = "admin"
mqtt_base_topic = "/abc"
