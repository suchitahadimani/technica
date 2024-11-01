from pyduino import *
import time


if __name__ == '__main__':
    
    print( 'Establishing connection to Arduino...')
    
    # if your arduino was running on a serial port other than '/dev/ttyACM0/'
    # declare: a = Arduino(serial_port='/dev/ttyXXXX')
    a = Arduino(serial_port='/dev/cu.SLAB_USBtoUART')
    
    # sleep to ensure ample time for computer to make serial connection 
    time.sleep(3)
    print( 'established!')
    
    # define our LED pin
    PIN = 4

    # initialize the digital pin as output
    a.set_pin_mode(PIN,'O')
    
    # allow time to make connection
    time.sleep(1)
    
    # turn LED on
    a.digital_write(PIN,1) 

    for i in range(0,1000):

        try:
            # Read the analog value from analogpin 6
            analog_val = a.analog_read(6)
            
            # print value in range between 0-100
            print('Light',analog_val)
            time.sleep(1)
        
        except KeyboardInterrupt:   
            break # kill for loop

    # to make sure we turn off the LED and close our serial connection
    print( 'CLOSING...')
    a.digital_write(PIN,0) # turn LED off 
    a.close()