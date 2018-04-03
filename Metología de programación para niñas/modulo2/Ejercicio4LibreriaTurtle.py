#Tomado de: https://michael0x2a.com/blog/turtle-examples
from turtle import *
import turtle


#Primer nivel

def dibujarLinea():
    pintorDeLinea = turtle.Turtle()

    pintorDeLinea.pencolor("#32D486")
    pintorDeLinea.forward(150)

    pintorDeLinea.pencolor("#D6305F")
    pintorDeLinea.forward(150)
    turtle.done()


dibujarLinea()





