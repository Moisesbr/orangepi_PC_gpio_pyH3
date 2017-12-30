#!/usr/bin/python
import time
import sys
import os

from pyA20.gpio import gpio
from pyA20.gpio import port
from pyA20.gpio import connector
gpio.init() #Initialize module. Always called first
gpio.initRPIO()
##input
reedSwitch = port.PA13
pluviometro1 = port.PA5
pluviometro2 = port.PA4
simpleFlag1 = port.PA16
simpleFlag2 = port.PA14
resetButton = port.PG11

##output
ledD5 = port.PG6
ledD6 = port.PG7
buzzer = port.PL11
power7v = port.PA15

gpio.setcfg(reedSwitch, gpio.INPUT)
gpio.setcfg(pluviometro1, gpio.INPUT)
gpio.setcfg(pluviometro2, gpio.INPUT)
gpio.setcfg(simpleFlag1, gpio.INPUT)
gpio.setcfg(simpleFlag2, gpio.INPUT)
gpio.setcfg(resetButton, gpio.INPUT)

gpio.setcfg(ledD5, gpio.OUTPUT)
gpio.setcfg(ledD6, gpio.OUTPUT)
gpio.setcfg(buzzer, gpio.OUTPUT)
gpio.setcfg(power7v, gpio.OUTPUT)

#definicoes de pinos da placa
#pin_led          = PA3
#pin_ding_button  = PA0
#pin_reset_button = PA2
#pin_input_opto1  = PC1
#pin_input_opto2  = PC2
#pin_relay1       = PG8
#pin_relay2       = PG9

print "Version 1.0"
while(True):
    print "reedSwitch  : " + str(gpio.input(reedSwitch))
    print "pluviometro1: " + str(gpio.input(pluviometro1))
    print "pluviometro2: " + str(gpio.input(pluviometro2))
    print "simpleFlag1 : " + str(gpio.input(simpleFlag1))
    print "simpleFlag2 : " + str(gpio.input(simpleFlag2))
    print "resetButton : " + str(gpio.input(resetButton))

    gpio.output(ledD5, 1)
    gpio.output(ledD6, 1)
    gpio.output(buzzer, 1)
    gpio.output(power7v, 1)

    time.sleep(7)

    gpio.output(ledD5, 0)
    gpio.output(ledD6, 0)
    gpio.output(buzzer, 0)
    gpio.output(power7v, 0)

    time.sleep(7)
