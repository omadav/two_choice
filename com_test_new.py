#import serial.tools.list_ports
# import pumps
#
#ports = serial.tools.list_ports.comports()
#print ports
#connected = []
#for element in ports:
#    connected.append(element.device)
#print("Connected COM ports: " + str(connected))
#
# pump = pumps.Pump(2)
import serial
ser = serial.Serial(port='COM3')
#
#import re
#import subprocess
#device_re = re.compile("Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
#df = subprocess.check_output("lsusb")
#devices = []
#for i in df.split('\n'):
#    if i:
#        info = device_re.match(i)
#        if info:
#            dinfo = info.groupdict()
#            dinfo['device'] = '/dev/bus/usb/%s/%s' % (dinfo.pop('bus'), dinfo.pop('device'))
#            devices.append(dinfo)
#print devices

