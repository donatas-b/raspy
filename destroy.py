#!/usr/bin/env python3
########################################################################
# Filename    : ButtonLED.py
# Description : Control led with button
# auther      : www.freenove.com
# modification: 2019/12/28
########################################################################
import RPi.GPIO as GPIO

if __name__ == '__main__':     # Program entrance
    ledPin = 11    # define ledPin
    buttonPin = 12    # define buttonPin

    GPIO.setmode(GPIO.BOARD)      # use PHYSICAL GPIO Numbering
    GPIO.setup(ledPin, GPIO.OUT)   # set ledPin to OUTPUT mode
      
    GPIO.output(11, GPIO.LOW)     # turn off led 
    GPIO.cleanup()                    # Release GPIO resource