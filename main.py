#!/usr/bin/env python3
from ev3dev.ev3 import *
from robo import Brabo
from CLPButtons import CLPButtons
from time import sleep

#Brabo is the robot's class name 
r = Brabo('outC', 'outD', 'in1', 'outA')

#set the distance of view of the robot
distance = 30

#start the clp buttons
btn = CLPButtons()

#wait until a button is pressed
btn.wait()

#this servers to make the robot wait a little while after the game starts
#because one of the rules of the competition prevent the robot from starting right away
#sleep(4.65)

#lower the ramp
r.ramp.run_to_rel_pos(position_sp=200, speed_sp=300, stop_action='brake')
#wait to the ramp is ready in place
sleep(0.6)
#reset the ramp
r.ramp.reset()
#lock the ramp
r.ramp.stop(stop_action='hold')

#main loop of the program
while True:
    #rotate forever around itself 
    r.rotate(800)
    
    #stops if a button is pressed
    btn.press_for_quit(r)

    #search for something in front of the robot
    while True:
        #stops if a button is pressed
        btn.press_for_quit(r)
        #print(r.us.distance_centimeters)
        #if something is in less then 30 centimeters of the robot
        if(r.sees_anything(distance)):
            #reset the motors
            r.reset()
            #hold the motors to stop rotating
            r.stop('hold')
            #escapes the loop
            break

    #it only gets here if there is something in front of the robot
    #in this case, the robot will go straight ahead forever
    r.run_forever(1050)
    
    #while something is in front of the robot
    while True:
        #stops if a button is pressed
        btn.press_for_quit(r)
        #print(r.us.distance_centimeters)
        #if something goes out of the sight of the robot
        if (not r.sees_anything(distance)):
            #the robot stops
            r.stop('hold')
            #it breaks the loop and the robot will start to rotate again
            break

