
Use git to get esptool from https://github.com/espressif/esptool.git

	git clone https://github.com/espressif/esptool.git	
	
Download firmware from http://micropython.org/download#esp8266	

Edit **flash.sh** and change **esp8266-20171101-v1.9.3.bin** to point to the firmware you just download.	

Edit **flash.sh** and change **/dev/tty.SLAB_USBtoUART** to use your serial port	

Connect your esp8266 board and verify your port and run the flash

	./flash.sh
	
