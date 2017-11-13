# IoT Esp8266 Using MicroPython http://micropython.org/
# Jason Peixoto
# http://www.iotecosystem.com
# IOT EcoSystem (c) is copyrighted by Jason Peixoto
# GNU GENERAL PUBLIC LICENSE 3
#
# Unless required by applicable law or agreed to in writing, this software is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# -------------------------------------------------------
# A0  - ADC0   - TOUT   | D0  - GPIO16 - USER  - WAKE
# RSV                   | D1  - GPIO05
# RSV                   | D2  - GPIO04
# D12 - GPIO10 - SDD3   | D3  - GPIO00 - FLASH
# D11 - GPIO09 - SDD2   | D4  - GPIO02 - TXD1
# INT - INT    - SDD1   | 3V3
# MO  - MOSI   - SDCMD  | GND
# MI  - MISO   - SDD0   | D5  - GPIO14         - HSPICLK
# SCK - SCLK   - SDCLK  | D6  - GPIO12         - HSPIQ
# GND                   | D7  - GPIO13 - RXD2  - HSPID
# 3V3                   | D8  - GPIO15 - TXD2  - HSPICS
# EN                    | D9  - GPIO03 - RXD0
# RST                   | D10 - GPIO01 - TXD0
# GND                   | GND
# 5V                    | 3V3
# ---------------------USB-------------------------------
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

# io names on right
TXD1 = GPIO02
RXD2 = GPIO13
TXD2 = GPIO15
RXD0 = GPIO03
TXD0 = GPIO01
HSPICLK = GPIO14
HSPIQ = GPIO12
HSPID = GPIO13
HSPICS = GPIO15

# io pins right
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


