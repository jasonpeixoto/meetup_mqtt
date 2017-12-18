# IoT Esp8266 Using MicroPython http://micropython.org/
# Jason Peixoto
# http://www.iotecosystem.com
# IOT EcoSystem (c) is copyrighted by Jason Peixoto
# GNU GENERAL PUBLIC LICENSE 3
#
# Unless required by applicable law or agreed to in writing, this software is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
#  HelTec esp32 board Lora
# ------------------------------------------------------------------------------------------------------
# 21 - GPIO21 - SDA    - V_SPI_HD             | 16 - GPIO16 - U2_RXD                         - OLED_RST
# 13 - GPIO13 - ADC2_4 - TOUCH4               | 17 - GPIO17 - U2_TXD
# 12 - GPIO12 - ADC2_5 - TOUCH5               | 04 - GPIO04 - ADC2_0    - HSPI_HD   - TOUCH0 - OLED_SDA
# 14 - GPIO14 - ADC2_6 - TOUCH6   - LORA_RST  | 02 - GPIO02 - ADC2_2    - HSPI_WP   - TOUCH2
# 27 - GPIO27 - ADC2_7 - TOUCH7   - LORA_MOSI | 15 - GPIO15 - ADC2_3    - HSPI_CS0  - TOUCH3 - OLED_SCL
# 26 - GPIO26 - ADC2_9 - DAC1     - LORA_IRQ  | 05 - GPIO05 - V_SPI_CSO - LORA_SCK
# 25 - GPIO25 - ADC2_8 - DAC2     - LED       | 18 - GPIO18 - V_SPI_CLK - LORA_CS
# 33 - GPIO33 - ADC1_5 - TOUCH9   - XTAL32    | 23 - GPIO23 - V_SPI_D
# 32 - GPIO32 - ADC1_4 - TOUCH8   - XTAL32    | 19 - GPIO19 - V_SPI_Q   - LORA_MISO          - U0_CTS
# 35 - GPIO35 - ADC1_7                        | 22 - GPIO22 - V_SPI_WP  - SCL                - U0_RTS
# 34 - GPIO34 - ADC1_6                        | 00 - GPIO00 - ADC_2_1   - CLK1      - TOUCH1 - BUTTON
# 39 - GPIO39 - ADC1_3 - SENSVN               | RST
# 38 - GPIO38 - ADC1_2 - CAPVN                | 01 - GPIO01 - TX        - CLX3               - U0_TXD
# 37 - GPIO37 - ADC1_1 - CAPVP                | 03 - GPIO03 - RX        - CLX2               - U0_RXD
# 36 - GPIO36 - ADC1_0 - SENSEVP              | GND
# 3V3                                         | 3V3
# 5V                                          | 5V
# GND                                         | GND
# --------------------------------------------USB-------------------------------------------------------
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



