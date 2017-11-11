import machine
import time
import iot_io

led_pin = iot_io.D1
button_pin = iot_io.D2

led = machine.Pin(led_pin, machine.Pin.OUT)
button = machine.Pin(button_pin, machine.Pin.IN)

while True:
    time.sleep_ms(200)
    led.value(button.value())