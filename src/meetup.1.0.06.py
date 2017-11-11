import machine
import time
import iot_io

button_pin = iot_io.D2       # d1

# create pin for each led
button = machine.Pin(button_pin, machine.Pin.IN)

while True:
    time.sleep_ms(200)
    print(button.value())