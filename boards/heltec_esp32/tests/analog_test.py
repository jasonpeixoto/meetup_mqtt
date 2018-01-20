# IoT Esp8266 Using MicroPython http://micropython.org/
# Jason Peixoto
# http://www.iotecosystem.com
# IOT EcoSystem (c) is copyrighted by Jason Peixoto
# GNU GENERAL PUBLIC LICENSE 3
#
# Unless required by applicable law or agreed to in writing, this software is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
import utime
import machine
import ssd1306

ADC1_0 = 36
ADC1_1 = 37
ADC1_2 = 38
ADC1_3 = 39
OLED_RST = 16
OLED_SDA = 4
OLED_SCL = 15


machine.Pin(ADC1_0, machine.Pin.IN)
machine.Pin(ADC1_1, machine.Pin.IN)
machine.Pin(ADC1_2, machine.Pin.IN)
machine.Pin(ADC1_3, machine.Pin.IN)

adc1 = machine.ADC(machine.Pin(ADC1_0))
adc2 = machine.ADC(machine.Pin(ADC1_1))
adc3 = machine.ADC(machine.Pin(ADC1_2))
adc4 = machine.ADC(machine.Pin(ADC1_3))

oled_rst = machine.Pin(OLED_RST, machine.Pin.OUT)
oled_rst.value(1);

i2c = machine.I2C(scl=machine.Pin(OLED_SCL), sda=machine.Pin(OLED_SDA))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

def readad(ad):
    total = 0;
    for i in range(25):
        total += ad.read();
    return int(total/25);

while(1):
    oled.fill(0)
    oled.text(str(readad(adc1)), 0,  0)
    oled.text(str(readad(adc2)), 0, 10)
    oled.text(str(readad(adc3)), 0, 20)
    oled.text(str(readad(adc4)), 0, 30)
    oled.show()
    utime.sleep_ms(100)
