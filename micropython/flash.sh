# IoT Esp8266 Using MicroPython http://micropython.org/
# Jason Peixoto
# http://www.iotecosystem.com
# IOT EcoSystem (c) is copyrighted by Jason Peixoto
# GNU GENERAL PUBLIC LICENSE 3
#
# Unless required by applicable law or agreed to in writing, this software is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
#!/bin/bash

comport=$1
firmware=$2

echo "Usage: flash.sh COMPORT FIRMWARE"
echo "Defaults: flash.sh $comport $firmware"

if [ $# -ne 2 ]; then
  comport="/dev/tty.SLAB_USBtoUART"
  firmware="esp8266-20171101-v1.9.3.bin"
fi
firmware="../$firmware"

echo "flash.sh $comport $firmware"

cd esptool
./esptool.py --port $comport erase_flash
./esptool.py --port $comport --baud 460800 write_flash --flash_size=detect 0 $firmware
