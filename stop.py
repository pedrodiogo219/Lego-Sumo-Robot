#!/usr/bin/env python3
import ev3dev.ev3 as ev3

ev3.LargeMotor('outD').stop(stop_action="coast")
ev3.LargeMotor('outB').stop(stop_action="coast")
ev3.LargeMotor('outA').stop(stop_action="coast")