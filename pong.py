# -*- coding: utf-8 -*-
"""
Created on Tue May  3 22:48:41 2022

@author: raushan
"""

import turtle

wn = turtle.Screen()
wn.title("Pong-I")

wn.bgcolor("black")
wn.setup(width=800, height=600)

wn.tracer(0)

# main game loop
while True:
    wn.update()

