import os
import re
import msvcrt
import usb.core
import usb.backend.libusb1
import usb.util


class _DeviceDescriptor(object):
    def __init__(self, idVendor, idProduct):
        self.bLength = 18
        self.bDescriptorType = usb.util.DESC_TYPE_DEVICE
        self.bcdUSB = 0x0200
        self.idVendor = idVendor
        self.idProduct = idProduct
        self.bcdDevice = 0x0001
        self.iManufacturer = 0
        self.iProduct = 0
        self.iSerialNumber = 0
        self.bNumConfigurations = 0
        self.bMaxPacketSize0 = 64
        self.bDeviceClass = 0xff
        self.bDeviceSubClass = 0xff
        self.bDeviceProtocol = 0xff
        self.bus = 1
        self.address = 1
        self.port_number = None
        self.port_numbers = None
        self.speed = None

def get_usb_device():
	#Vendor and Product id = USB\VID_064B&PID_7823&REV_0100
    try:
    	#S'ha de fer de la manera següent pq sino es pensa que es 'find_all'
    	dev = usb.core.find(idVendor= 0x064B, idProduct= 0x7823)

    	if dev is None:
    		raise ValueError ('Device not found')
    	# set the active configuration. With no arguments, the first
    	# configuration will be the active one
    	dev.set_configuration()
    	#for cfg in dev:
    	#	print("Hola")
    	#sys.stdout.write(str(cfg.bConfigurationValue) + '\n')

    	# get an endpoint instance
    	print("Hola2")
    	cfg = dev.get_active_configuration()
    	intf = cfg[(0,0)]
    	print("Hola3")

    	#End Point
    	ep = usb.util.find_descriptor(
    		intf,
    		# match the first OUT endpoint
    		custom_match = \
    		lambda e: \
    		usb.util.endpoint_direction(e.bEndpointAddress) == \
    		usb.util.ENDPOINT_OUT)
    	assert ep is not None

    	# write the data
    	ep.write('test')
    	print("Hola4")

    except Exception as ex:
    	template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    	message = template.format(type(ex).__name__, ex.args)
    	print (message)

quit = False
while not quit:
	os.system('cls' if os.name == 'nt' else 'clear')
	print("Main menu")
	x = input()
	if x == "1":
		get_usb_device()
		
	else:
		quit = True

	print("Press any key to continue.")
	msvcrt.getch()