#Paul Ambrose 25th April 2020
#Temperature Checking Programe.  Uses temp sensor in pi hat.  Changes colours on pixels on pihat based on the temperature.

from sense_hat import SenseHat
import time
import os

def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

    cpu_temp = getCPUtemperature()
    return cpu_temp

def main():
  while True:
    sense = SenseHat()
    test_temp = sense.get_temperature()
    cpu_temp = getCPUtemperature()
    
    temp_calibrated = test_temp - ((float(cpu_temp) - test_temp)/5.466)

    if float(temp_calibrated) > 0 and float(temp_calibrated) <= 16:
      O  = [0, 0, 255]
    if float(temp_calibrated)  > 16 and float(temp_calibrated)  <= 20:
      O  = [225, 165, 0]
    if float(temp_calibrated)  > 20 and float(temp_calibrated)  <= 23:
      O  = [255, 100, 165]
    if float(temp_calibrated)  >= 24:
      O  = [150, 0, 0]
  
    total = [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O]
    sense.set_pixels(total)

    time.sleep(5)
    print(temp_calibrated)

if __name__ == "__main__":
  main()