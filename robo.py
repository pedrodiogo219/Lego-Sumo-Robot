import ev3dev.ev3 as ev3
from time import sleep
class Brabo(object):
    
    def __init__(self, outMe, outMd, inUs, inRmp):
        #declare all the motors and sensors
        self.me = ev3.LargeMotor(outMe)
        self.md = ev3.LargeMotor(outMd)
        self.us = ev3.UltrasonicSensor(inUs)
        self.ramp = ev3.LargeMotor(inRmp)

        #reset everything and holds everything into position
        self.ramp.reset()
        self.reset()
        self.stop('hold')    

    def reset(self):
        self.me.reset()
        self.md.reset()

    def run_forever(self, speed):
        self.me.run_forever(speed_sp = speed)
        self.md.run_forever(speed_sp = speed)

    def run_quant(self, quant, speed):
        self.me.run_to_rel_pos(speed_sp=speed, position_sp=quant, stop_action='hold')
        self.md.run_to_rel_pos(speed_sp=speed, position_sp=quant, stop_action='hold')
        while self.md.state != ['holding']:
            pass
        
    def stop(self, action):
        self.me.stop(stop_action=action)
        self.md.stop(stop_action=action)
        self.ramp.stop(stop_action=action)
    
    def rotate(self, speed):
        self.me.run_forever(speed_sp =  speed, stop_action='brake')
        self.md.run_forever(speed_sp = -speed, stop_action='brake')
    
    def ramp_push(self):
        self.ramp.run_to_abs_pos(position_sp=-30, speed_sp=1000, stop_action='hold')
        sleep(0.2)
        self.ramp.run_to_abs_pos(position_sp=  0, speed_sp= 300, stop_action='hold')
        sleep(0.5)

    def sees_anything(self):
        return (self.us.distance_centimeters <= float(20))
    
    def come_back(self):
        self.me.run_to_abs_pos(position_sp = 0, speed_sp = 300)
        self.md.run_to_abs_pos(position_sp = 0, speed_sp = 300)
        while self.me.state != ['holding']:
            pass
    


