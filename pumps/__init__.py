# Class for controlling syringe pumps with RS-232 connectivity.
# Implementation is designed to be modular to enable operation of pumps
# from a variety of manufacturers.
# 
# Based on pumps.m master/slave interface for Matlab by ...
# Lloyd Ung
#
# Author: Wolfgang M. Pauli
# created: 2015-11-28
#
#    This is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This software is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright 2014 California Institute of Technology.


import serial, glob, sys, time
import logging

logger = logging.getLogger() 
logger.setLevel(getattr(logging, 'INFO'))

def scan():
    ''' get available ports '''
    available = []
    if sys.platform == 'linux2':
        print "this is a linux2 system"
        # scan for available ports. return a list of device names.
        ports = glob.glob('/dev/ttyUSB*') + glob.glob('/dev/ttyS*') 
        print "Ports: " + str(ports)
        i = 0
        for port in ports:
            try:
                s = serial.Serial(port)
                available.append( (i, s.portstr))
                i += 1
                s.close()
                print "Port: " + port
            except serial.SerialException:
                pass
    else: # this may or may not work in windows
        # scan for available ports. return a list of tuples (num, name)
        print "This is a Windows system"
        for i in range(256):
            try:                
                s = serial.Serial()
                available.append( (i, s.portstr))
                s.close()
                #print "Port: " + i
            except serial.SerialException:
                pass
    return available

class Pump:
    # Serial link parameters
    newEraSerialConfig = dict([('BaudRate',19200),('DataBits',8),
                               ('FlowControl','none'),('Parity','none'),('StopBits',1),
                               ('Terminator','CR')])

    # Command String
    newEraCommandString = dict([('diameter','DIA'),('run','RUN'),('stop','STP'),('rate','RAT'),
                                  ('volume','VOL'),('direction','DIR'),('dispensed','DIS'),
                                  ('clearDispense','CLD'),('safe','SAF'),('version','VER')])
    
    # Syringe data table
    syringeData = []
        
    # Constants
    serialWaitTime = .5 # units of seconds

    # Serial handle
    serialHandle = ''

    # Command String - holds the structure of commands appropriate for
    # a certain model of pump.
    cStr = []

    def __init__(self, port):
        if type(port) != str:
            print('The input argument must be a string, e.g. \'/dev/ttyUSB0\'');
        else:
            print('Using port: %s' % port)
        try:
            self.serialHandle = serial.Serial()
            self.serialHandle.baudrate = self.newEraSerialConfig['BaudRate']
            # self.serialHandle.CR = self.newEraSerialConfig['Terminator']
            self.serialHandle.port = port
            # self.serialHandle.FlowControl = 'none'
            # self.serialHandle.Terminator = 'CR'
            # self.serialHandle.DataBits = 8
            # self.serialHandle.Parity = 'none'
            # self.serialHandle.StopBits = 1
            self.serialHandle.open()
        except serial.SerialException:
            print ('Desired port is not available.')
            raise
    


    def delete(self):
        """ delete serial port object """
        print ("Closing serial port: %s" % self.serialHandle.port)
        self.serialHandle.close()
        self.serialHandle = ''



    def clearDispense(self, direction, address=0):
        """ Set/Query volume to dispense """
        cmd = self.newEraCommandString.clearDispense

        if direction.upper() == 'INF' or direction.upper() == 'WDR':
            cmd += " " + str.upper(direction)
        else:
            print ("Not a valid direction.")
            return False
        value = self.interface(cmd, address)
        return value
    


    def run(self,address=0):
        """ run the pump as set """
        cmd = self.newEraCommandString['run']
        value = self.interface(cmd, address)
        return value



    def stop(self, address=0):
        """ send command to stop pumping """
        cmd = self.newEraCommandString['stop']
        value = self.interface(cmd, address)

        return value



    def volume(self, value='', address=0):
        # Set/Query volume to dispense (only set at this point)
        cmd = self.newEraCommandString['volume']
        if value != '':
            if value >= 100:
                formatString = '%4.1f'
            elif value >= 10:
                formatString = '%4.2f'
            else:
                formatString = '%4.3f'
            value = formatString % value

        cmd = cmd + " " + value

        return_value = self.interface(cmd, address)
        if value == '':
            return_value = "Volume: " + return_value.strip('\x0200S').strip('\x03')
        return return_value




    def dispensed(self, address=0):
        """ get how much has been dispensed """ 
        cmd = self.newEraCommandString['dispensed']
        return_value = self.interface(cmd, address)
        if value == '':
            return_value = "Dispensed: " + return_value.strip('\x0200S').strip('\x03')
        return return_value



    def rate(self, value='', unit='MM', address=0):
        """set/get at which rate to pump. Note: getting this value doesn't
        work for some reason, but setting it is fine"""
        cmd = self.newEraCommandString['rate']
        if value != '':
            if value >= 1000:
                formatString = '%4.0f'
            elif value >= 100:
                formatString = '%4.1f'
            elif value >= 10:
                formatString = '%4.2f'
            else:
                formatString = '%4.3f'
            value = formatString % value
       
        cmd = cmd + " " + value + " " + unit

        return_value = self.interface(cmd, address)
        if value == '':
            return_value = "Rate: " + return_value.strip('\x0200S').strip('\x03') + unit + " (querying doesn't work)"
        return return_value




    def direction(self, direction='', address=0):
        """ set direction in which we want to move syringe """
        cmd = self.newEraCommandString['direction']
        
        cmd = cmd + " " + direction.upper()
        
        return_value = self.interface(cmd, address)

        if direction == '':
            return_value = "Direction: " + return_value.strip('\x0200S').strip('\x03')
        return return_value




    def diameter(self, value='', address=0):
        """ get/set diameter of syringe """
        cmd = self.newEraCommandString['diameter']
 
        if value != '':
            if value >= 100:
                formatString = '%4.1f'
            elif value >= 10:
                formatString = '%4.2f'
            else:
                formatString = '%4.3f'
            value = formatString % value

        cmd = cmd + " " + value

        return_value = self.interface(cmd, address)
        if value == '':
            return_value = "Diameter: " + return_value.strip('\x0200S').strip('\x03')
        return return_value



    def version(self, address=0):
        """ get version of pump """
        cmd = self.newEraCommandString['version']
 
        return_value = self.interface(cmd, address)
        return_value = "Version: " + return_value.strip('\x0200S').strip('\x03')
        return return_value



    def interface(self, cmd, address):
        """ generic function to interact with pumps"""
        address = '%02d' % address

        cmd = address + cmd + '\r\n'

        logger.debug(cmd)
        # send command to serial port
        self.serialHandle.writelines(cmd)
        
        # Wait for bytes to appear at the port.
        time.sleep(self.serialWaitTime)

        return self.serialHandle.read(self.serialHandle.inWaiting())


if __name__ == "__main__":
    p = Pump('/dev/ttyUSB0')

    s = p.volume(0.75)  # how much to dispense
    s = p.diameter(26.77) # diameter of syringe
    s = p.rate(60) # how fast
    s = p.direction('INF') # pump (not suck) liquid

    s = p.volume(0.75,address=1)  # how much to dispense
    s = p.diameter(26.77,address=1) # diameter of syringe
    s = p.rate(60,address=1) # how fast
    s = p.direction('INF',address=1) # pump (not suck) liquid

    print(p.volume()) # how much to dispense
    print(p.diameter()) # diameter of syringe
    print(p.rate()) # how fast
    print(p.direction()) # pump (not suck) liquid
    

    s = p.run(0)
    s = p.run(1)
    p.delete()

