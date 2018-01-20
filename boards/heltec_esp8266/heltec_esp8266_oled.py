# IoT Esp8266 Using MicroPython http://micropython.org/
# Jason Peixoto
# http://www.iotecosystem.com
# IOT EcoSystem (c) is copyrighted by Jason Peixoto
# GNU GENERAL PUBLIC LICENSE 3
#
# Unless required by applicable law or agreed to in writing, this software is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# ----------------------------------------------------------------------
# RST                                  | A00 - 17 - GPIO17 - ADC - TOUT
# D02 - 04 - GPIO04 - SDA  - OLED_RST  | D00 - 16 - GPIO16 - WAKE
# RST                                  | D05 - 14 - GPIO14 - HSPI   - CLK - OLED_SCL
# D09 - 03 - GPIO03 - RXD0             | D06 - 12 - GPIO12 - HSPIQ  - MISO
# D10 - 01 - GPIO01 - TXD0 - CS1       | D07 - 13 - GPIO13 - HSPID  - MOSI - RXD2 - CTS0
# D01 - 05 - GPIO05 - SCL              | D08 - 15 - GPIO15 - HSPICS - CS   - TXD2 - RTS0
# DTR                                  | D04 - 02 - GPIO02 - TXD2   - OLED_SDA
# CTS                                  | D03 - 00 - GPIO00 - CS2
# GND                                  | GND
# 3V3                                  | 3V3
# 5V                                   | 5V
# GND                                  | GND
# ------------------------------------USB-------------------------------
GPIO00 = 0
GPIO01 = 1
GPIO02 = 2
GPIO03 = 3
GPIO04 = 4
GPIO05 = 5
GPIO06 = 6
GPIO07 = 7
GPIO08 = 8
GPIO09 = 9
GPIO10 = 10
GPIO11 = 11
GPIO12 = 12
GPIO13 = 13
GPIO14 = 14
GPIO15 = 15
GPIO16 = 16
GPIO17 = 17

# io pins
A0 = GPIO17
D0 = GPIO16
D1 = GPIO05
D2 = GPIO04
D3 = GPIO00
D4 = GPIO02
D5 = GPIO14
D6 = GPIO12
D7 = GPIO13
D8 = GPIO15
D9 = GPIO03
D10 = GPIO01
D11 = GPIO09
D12 = GPIO10

# io names
SDA = OLED_RST = D2
RXD0 = D9
TXD0 = CS1 = D10
ADC = TOUT = A0
WAKE = GPIO16
HSPI = CLK = OLED_SCL = D5
HSPIQ = MISO = D6
HSPID = MOSI = RXD2 = CTS0 = D7
HSPICS = CS = TXD2 = RTS0 = D8
TXD2 = OLED_SDA = D4
CS2 = D3



