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
