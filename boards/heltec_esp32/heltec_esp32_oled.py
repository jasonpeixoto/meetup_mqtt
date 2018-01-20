# IoT Esp8266 Using MicroPython http://micropython.org/
# Jason Peixoto
# http://www.iotecosystem.com
# IOT EcoSystem (c) is copyrighted by Jason Peixoto
# GNU GENERAL PUBLIC LICENSE 3
#
# Unless required by applicable law or agreed to in writing, this software is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
#  HelTec esp32 oled board
# ------------------------------------------------------------------------------------------------------
# 21 - GPIO21 - SDA    - V_SPI_HD                     | 36 - GPIO36 - ADC1_0 - SENSEVP
# 22 - GPIO22 - SCL    - V_SPI_WP  - U0_RTS           | 37 - GPIO37 - ADC1_1 - CAPVP
# 19 - GPIO19 - MISO   - V_SPI_Q   - U0_CTS           | 38 - GPIO38 - ADC1_2 - CAPVN
# 23 - GPIO23 - MISI   - V_SPI_D                      | 39 - GPIO39 - ADC1_3 - SENSVN
# 18 - GPIO18 - SCK    - V_SPI_CLK                    | 34 - GPIO34 - ADC1_6
# 05 - GPIO05          - V_SPI_CS0                    | 35 - GPIO35 - ADC1_7
# 17 - GPIO17 - U2_TXD                                | 32 - GPIO32 - ADC1_4 - TOUCH8   - XTAL32
# 16 - GPIO16 - U2_RXD - OLED_RST                     | 33 - GPIO33 - ADC1_5 - TOUCH9   - XTAL32
# 04 - GPIO04 - ADC2_0 - TOUCH0 - HSPI_HD  - OLED_SDA | 25 - GPIO25 - ADC2_8 - DAC2     - LED
# 00 - GPIO00 - ADC2_1 - TOUCH1 - BUTTON   - CLK1     | 26 - GPIO26 - ADC2_9 - DAC1
# 02 - GPIO02 - ADC2_2 - TOUCH2 - HSPI_WP  - CS       | 27 - GPIO27 - ADC2_7 - TOUCH7
# 15 - GPIO15 - ADC2_3 - TOUCH3 - HSPI_CS0 - OLED_SCL | 14 - GPIO14 - ADC2_6 - TOUCH6
# 03 - GPIO03 - RX     - U0_RXD - CLX2                | 12 - GPIO12 - ADC2_5 - TOUCH5
# 01 - GPIO01 - TX     - U0_TXD - CLX3                | 13 - GPIO13 - ADC2_4 - TOUCH4
# GND                                                 | RST
# 3V3                                                 | 3V3
# 5V                                                  | 5V
# GND                                                 | GND
# ---------------------------------------------------USB-------------------------------------------------------
GPIO00 = 0
GPIO01 = 1
GPIO02 = 2
GPIO03 = 3
GPIO04 = 4
GPIO05 = 5
GPIO12 = 12
GPIO13 = 13
GPIO14 = 14
GPIO15 = 15
GPIO16 = 16
GPIO17 = 17
GPIO18 = 18
GPIO19 = 19
GPIO21 = 21
GPIO22 = 22
GPIO23 = 23
GPIO25 = 25
GPIO26 = 26
GPIO27 = 27
GPIO32 = 32
GPIO33 = 33
GPIO34 = 34
GPIO35 = 35
GPIO36 = 36
GPIO37 = 37
GPIO38 = 38
GPIO39 = 39

# io names on right
U2_RXD = OLED_RST = GPIO16
U2_TXD = GPIO17
ADC2_0 = HSPI_HD = TOUCH0 = OLED_SDA = GPIO04
ADC2_2 = HSPI_WP = TOUCH2 = GPIO02
ADC2_3 = HSPI_CS0 = TOUCH3 = OLED_SCL = GPIO15
V_SPI_CSO = LORA_SCK = GPIO05
V_SPI_CLK = LORA_CS = GPIO18
V_SPI_D = GPIO23
V_SPI_Q = LORA_MISO = U0_CTS = GPIO19
V_SPI_WP = SCL = U0_RTS = GPIO22
ADC_2_1 = CLK1 = TOUCH1 = BUTTON = GPIO00
TX = CLX3 = U0_TXD = GPIO01
RX = CLX2 = U0_RXD = GPIO03


# io pins left
SDA = V_SPI_HD = GPIO21
ADC2_4 = TOUCH4 = GPIO13
ADC2_5 = TOUCH5 = GPIO12
ADC2_6 = TOUCH6 = LORA_RST = GPIO14
ADC2_7 = TOUCH7 = LORA_MOSI = GPIO27
ADC2_9 = DAC1 = LORA_IRQ = GPIO26
ADC2_8 = DAC2 = LED = GPIO25
ADC1_5 = TOUCH9 = XTAL32 = GPIO33
ADC1_4 = TOUCH8 = XTAL32 = GPIO32
ADC1_7 = GPIO35
ADC1_6 = GPIO34
ADC1_3 = SENSVN = GPIO39
ADC1_2 = CAPVN = GPIO38
ADC1_1 = CAPVP = GPIO37
ADC1_0 = SENSEVP = GPIO36



