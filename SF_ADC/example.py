"""
Copyright (c) 2012-2013 Limor Fried, Kevin Townsend and Mikey Sklar for Adafruit Industries. All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the
following conditions are met: * Redistributions of source code must retain the above copyright notice, this list
of conditions and the following disclaimer. * Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided
with the distribution. * Neither the name of the nor the names of its contributors may be used to endorse or promote
products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
IN NO EVENT SHALL BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

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


