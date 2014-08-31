door-phone-hack
===============

This is a hack that allows you to open the front door to an apartment building with help of a smart phone's browser.

By adding a Relay over the button that opens the block’s front door it is possible to control the door by using a raspberry pi, or any other microcontroller for that matter. 

## Installing dependencies.

You only need [RPi.GPIO]:

	$ wget http://pypi.python.org/packages/source/R/RPi.GPIO/RPi.GPIO-0.1.0.tar.gz
  	$ tar zxf RPi.GPIO-0.1.0.tar.gz
  	$ cd RPi.GPIO-0.1.0
  	$ sudo python setup.py install
  	
## Run at boot

To make the script door.py run at boot, add 'python /"path"/DoorOpenLED/door.py' to /etc/rc.local.

## Circuit Setup

A description of the circuit that is needed is described in circuit_door.png. In the script door.py pin 12 (GPIO 18) is used. The RSPI is also used for power supply and ground. The Relay should be connected parallel to the button that open's the door.

## Network Setup

This hack will not describe the implementation of an website or any more sophisticated network tool to make this hack become safer. 

To make the hack work with a global IP you need to redirect your routers traffic to the RSPI's local IP with the correct port (port 9095 in this example). Also using services like noip.com will give you an URL. This will be essential if you are to use this hack from outside your home.


