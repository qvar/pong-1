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

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# paddle B
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(350,0)

# main game loop
while True:
    wn.update()

