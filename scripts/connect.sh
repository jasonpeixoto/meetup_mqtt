#!/bin/bash
# IoT Esp8266 Using MicroPython http://micropython.org/
# Jason Peixoto
# http://www.iotecosystem.com
# IOT EcoSystem (c) is copyrighted by Jason Peixoto
# GNU GENERAL PUBLIC LICENSE 3
#
# Unless required by applicable law or agreed to in writing, this software is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#

comport=$1
if [ $# -ne 1 ]; then
  # default for linux you can change it
  comport="/dev/tty.SLAB_USBtoUART"
fi
echo "rshell --buffer-size=30 -p $comport"
rshell --buffer-size=30 -p $comport
