#!/usr/bin/env python3
from ev3dev.ev3 import *
from robo import Brabo
from CLPButtons import CLPButtons
from time import sleep

r = Brabo('outD', 'outB', 'in1', 'outA')

btn = CLPButtons()
btn.wait()

r.ramp.run_to_rel_pos(position_sp=170, speed_sp=300, stop_action='hold')
sleep(0.6)
r.ramp.reset()
r.ramp.stop(stop_action='hold')


while True:
    r.rotate(300)
    
    btn.press_for_quit(r)

    while True:
        btn.press_for_quit(r)
        print(r.us.distance_centimeters)
        if(r.sees_anything()):
            r.reset()
            r.stop('hold')
            break
    
    r.run_forever(300)

    while True:
        btn.press_for_quit(r)
        print(r.us.distance_centimeters)
        if (not r.sees_anything) or r.md.position > 600:
            r.stop('hold')
            r.come_back()
            break
        r.ramp_push()
        

