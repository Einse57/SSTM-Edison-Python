#!/usr/bin/python

import time, signal, sys
from SF_ADC import ADS1x15

def signal_handler(signal, frame):
    print 'You pressed Ctrl+C!'
    sys.exit(0)
    
signal.signal(signal.SIGINT, signal_handler)
#print 'Press Ctrl+C to exit'

# Select the gain
# gain = 6144  # +/- 6.144V
gain = 4096  # +/- 4.096V
# gain = 2048  # +/- 2.048V
# gain = 1024  # +/- 1.024V
# gain = 512   # +/- 0.512V
# gain = 256   # +/- 0.256V

# Select the sample rate
# sps = 128   # 128 samples per second
sps = 250   # 250 samples per second
# sps = 490   # 490 samples per second
# sps = 920   # 920 samples per second
# sps = 1600  # 1600 samples per second
# sps = 2400  # 2400 samples per second
# sps = 3300  # 3300 samples per second

# Initialise the ADC
# Full options = ADCS1x15(address=0x48, I2CPort=1)
adc = ADS1x15()

# Read channel 0 in single-ended mode using the settings above
volts = adc.readADCSingleEnded(0, gain, sps) / 1000
print "%.6f" % (volts)
volts = adc.readADCSingleEnded(1, gain, sps) / 1000
print "%.6f" % (volts)
volts = adc.readADCSingleEnded(2, gain, sps) / 1000
print "%.6f" % (volts)
volts = adc.readADCSingleEnded(3, gain, sps) / 1000
print "%.6f" % (volts)

# To read channel 3 in single-ended mode, +/- 1.024V, 860 sps use:
# volts = adc.readADCSingleEnded(3, 1024, 860)


