"""
Copyright (c) 2015, Andrew Lamkin
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

#!/usr/bin/python

import time
import datetime
from datetime import datetime
from SF_9DOF.SF_9DOF import IMU
from SF_ADC.SF_ADC import ADS1x15

# Timing variables
ADC_lastread = 0
IMU_lastread = 0
LOG_lastlog = 0

ADC_rate = 100      # 10 Hz = 1/10s = 0.1s = 100 milliseconds
IMU_rate = 100      # 10 Hz = 1/10s = 0.1s = 100 milliseconds
LOG_rate = 100      # 10 Hz = 1/10s = 0.1s = 100 milliseconds

# Set up logging
today = datetime.now()
log_name = today.strftime("%y%b%d_%H%M%S") + ".txt"
log_file = open(log_name, "a")
today = datetime.now()

# Initial log write
log_file.write("Sensor Log: " + str(today.strftime("%d-%b-%y @ %H:%M:%S")) + "\n")
log_file.close()

# Set up devices
#### Create IMU object ####
# To select a specific I2C port, use IMU(n). Default is 1.
imu = IMU() 
# Initialize IMU
imu.initialize()
# Enable accel, mag, gyro, and temperature
imu.enable_accel()
imu.enable_mag()
imu.enable_gyro()
#imu.enable_temp()
# Set range on accel, mag, and gyro
# Specify Options: "2G", "4G", "6G", "8G", "16G"
imu.accel_range("2G")       # leave blank for default of "2G" 
# Specify Options: "2GAUSS", "4GAUSS", "8GAUSS", "12GAUSS"
imu.mag_range("2GAUSS")     # leave blank for default of "2GAUSS"
# Specify Options: "245DPS", "500DPS", "2000DPS" 
imu.gyro_range("245DPS")    # leave blank for default of "245DPS"

#### Create ADC object ####
# Full options = ADCS1x15(address=0x48, I2CPort=1)
adc = ADS1x15()
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

print("**Sensor Logging Active")

#### Main Work ####
while True:
    try:
        # Time locked loop
        millis = int(round(time.time() * 1000))
        
        if (millis - ADC_lastread >= ADC_rate):
            # Read the ADC module (line, gain, sps)
            ADC0 = adc.readADCSingleEnded(0, gain, sps) / 1000
            ADC1 = adc.readADCSingleEnded(1, gain, sps) / 1000
            ADC2 = adc.readADCSingleEnded(2, gain, sps) / 1000
            ADC3 = adc.readADCSingleEnded(3, gain, sps) / 1000
            # Update timing
            ADC_lastread = millis

        if (millis - IMU_lastread >= IMU_rate):
            # Read the IMU Module
            imu.read_accel()
            imu.read_mag()
            imu.read_gyro()
            #imu.readTemp()
            # Update timing
            IMU_lastread = millis
        
        if (millis - LOG_lastlog >= LOG_rate):
            # Logging statement
            log_file = open(log_name, "a")
            log_file.write(str(millis) + ", " + str(imu.ax) + ", " + str(imu.ay) + ", " + str(imu.az) + ", " \
                                              + str(imu.mx) + ", " + str(imu.my) + ", " + str(imu.mz) + ", " \
                                              + str(imu.gx) + ", " + str(imu.gy) + ", " + str(imu.gz) + ", " \
                                              + str(ADC0) + ", " + str(ADC1) + ", " + str(ADC2) + ", " + str(ADC3) + "\n")
            log_file.close()
            # Update timing
            LOG_lastlog = millis
        
    except KeyboardInterrupt:
        #Try to shut down cleanly
        log_file.close()
        print("**Closing Down Sensor Logging")
        break
    

