#Paul Ambrose 25th April 2020
#Temperature Checking Programe.  Uses temp sensor in pi hat.  Changes colours on pixels on pihat based on the temperature.

from sense_hat import SenseHat
import time

def main():
  while True:
    sense = SenseHat()
    sense.clear()
    test_temp = sense.get_temperature()

    if float(test_temp) > 0 and float(test_temp) <= 16:
      O  = [0, 0, 255]
    if float(test_temp)  > 16 and float(test_temp)  <= 20:
      O  = [225, 165, 0]
    if float(test_temp)  > 20 and float(test_temp)  <= 23:
      O  = [255, 100, 165]
    if float(test_temp)  >= 24:
      O  = [150, 0, 0]
  
    total = [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O]
    sense.set_pixels(total)

    time.sleep(60) 

if __name__ == "__main__":
  main()
