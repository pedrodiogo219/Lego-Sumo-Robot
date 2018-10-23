from ev3dev.ev3 import *
import sys 

class CLPButtons(Button):
    
    def wait(self):
        while not self.any():
            pass

    def press_for_quit(self, robot):
        if(self.any()):
            robot.reset()
            robot.ramp.stop(stop_action='coast')
            sys.exit(0)
