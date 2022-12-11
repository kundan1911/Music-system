import pygame
from time import sleep
import RPi.GPIO as GPIO
from gpiozero import Button
from gpiozero import LED
#  AvailableDigitalPins: [4 7 8 9 10 11 12 13 14 15 17 18 22 23 24 25 27 30 31]
def color_code(code):
    if code==0:
        led[0].on()
        led[1].on()
        led[3].on()
        led[4].on()
    
    led[0].off()
    led[1].off()
    led[3].off()
    led[4].off()
    led[2].off()
    return
GPIO.setmode(GPIO.BOARD)

pygame.init()
# 4 ,5,6,7, 8, 9, 10, 11, 12, 13,
# 14, 15,16, 17, 18, 22, 23, 24, 25, 27, 30, 31
buttoncount=1
ledcount=1
buttons=list();
Leds=list();
j=4;
for i in range(buttoncount):
    button=Button(j)
    buttons.append(button);
    j=j+1

for i in range(ledcount):
    led=LED(j);
    Leds.append(led);
    j=j+1;
button_sounds = {buttons[0]:pygame.mixer.Sound("/home/pi/A1_group_2_project/samples/D_PowerChords_95_SP.wav")}

while(True):
    j=0;
    for button, sound in button_sounds.items():
        if button.is_pressed:
            sound.play()
            color_code(j)
        j=j+1


