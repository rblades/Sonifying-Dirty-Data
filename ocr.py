from difflib import SequenceMatcher

import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GREEN_LED = 18
RED_LED = 23
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)
  
  text1 = 'ocr.txt'
  text2 = 'conversion.txt'
  m = SequenceMatcher(None, text1, text2)
  print m.ratio()*100
  
  weight = m.ratio()*100
  
  if weight > 70:
        GPIO.output(GREEN_LED, True)
        GPIO.output(RED_LED, False)
    else:
        GPIO.output(GREEN_LED, False)
        GPIO.output(RED_LED, True)