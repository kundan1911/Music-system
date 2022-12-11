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
    elif code==1:
        led[0].on()
        led[1].on()  
    elif code==2:
        led[2].on()
        led[3].on()
        led[4].on()
    elif code==3:
        led[0].on()
        led[2].on()
        led[4].on()
    elif code==4:
        led[0].on()
        led[1].on()
        led[3].on()
    elif code==5:
        led[2].on()
        led[1].on()
        led[3].on()
    elif code==6:
        led[2].on()
        led[3].on()
    elif code==7:
        led[0].on()
        led[1].on()
        led[4].on()
        led[2].on()
    elif code==8:
        led[0].on()
        led[1].on()
        led[3].on()
        led[2].on()
    else:
        led[0].on()
        led[1].on()
        led[3].on()
        led[4].on()
        led[2].on()
    led[0].off()
    led[1].off()
    led[3].off()
    led[4].off()
    led[2].off()
    return
GPIO.setmode(GPIO.BCM)

pygame.init()
# 4 ,5,6,7, 8, 9, 10, 11, 12, 13,
# 14, 15,16, 17, 18, 22, 23, 24, 25, 27, 30, 31
buttoncount=8
ledcount=5
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
button_sounds = {buttons[0]: pygame.mixer.Sound("/home/pi/A1_group_2_project/samples/34_Fm_Guitar_SP_222_01.wav"),
                 buttons[1]: pygame.mixer.Sound("/home/pi/A1_group_2_project/samples/A_StringGuitar_01_710.wav"),
                 buttons[2]: pygame.mixer.Sound("/home/pi/A1_group_2_project/samples/A#_Guitar_412_SP_01.wav"),
                 buttons[3]: pygame.mixer.Sound("/home/pi/A1_group_2_project/samples/C#m_BMaj9ShortChordAcGuitar_01_577.wav"),
                 buttons[4]:pygame.mixer.Sound("/home/pi/A1_group_2_project/samples/D_PowerChords_95_SP.wav"),
                 buttons[5]:pygame.mixer.Sound("/home/pi/A1_group_2_project/samples/Dm_WahShortGuitar_725.wav"),
                 buttons[6]:pygame.mixer.Sound("/home/pi/A1_group_2_project/samples/Gm_Guitar_412_SP_02.wav"),
                 buttons[7]:pygame.mixer.Sound("/home/pi/A1_group_2_project/samples/GuitarAcou_05_46_SP.wav"),
                #  buttons[8]:pygame.mixer.Sound("/home/pi/A1_group_2_project/samples/B_MutedNoteGuitar_725.wav"),
                #  buttons[9]:pygame.mixer.Sound("/home/pi/A1_group_2_project/samples/GuitarThatNote_01_695.wav")
                }

while(True):
    j=0
    for button, sound in button_sounds.items():
        if button.is_pressed:
            sound.play
            color_code(j)
        j=j+1


