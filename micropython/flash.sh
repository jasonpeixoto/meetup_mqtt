# Flash esp8266 by Jason Peixoto 
# IOT EcoSystem (c) 
# www.iotecosystem.com
#
# GNU GENERAL PUBLIC LICENSE 3
#
cd esptool
./esptool.py --port /dev/tty.SLAB_USBtoUART erase_flash 
./esptool.py --port /dev/tty.SLAB_USBtoUART --baud 460800 write_flash --flash_size=detect 0 ../esp8266-20171101-v1.9.3.bin

