import matplotlib.pyplot as plt
import numpy as np
import math

def Velocity(i):

    T = 297.15
    R = 8.3145
    mco2 = 44.01/1000
    mo2 = 15.999*2/1000
    mar = 39.948/1000
    mn2 = 28.0134/1000
    mh20 = 18.0153/1000
    xar = 0.9/100
    xn2 = 0.781
    xh20 = 0.924/100
    speed_exhaled = 342.6


    ms = xn2 * mn2 + xar * mar + xh20 * mh20 + i * mco2 + mo2 * (1-(i + xar + xh20 + xn2))

    gamma = (xn2 * mn2 * 3.5 + xar * mar * 2.5 + xh20 * mh20 * 4 + i * mco2 * 4.46 + mo2 * (1-(i + xar + xh20 + xn2)) * 3.5)/(xn2 * mn2 * 2.5 + xar * mar *1.5 + xh20 * mh20 * 3 + i * mco2 * 3.46 + mo2 * (1-( i + xar + xh20 + xn2 ))*2.5 )
    velocity= (gamma*R*T/ms)**(1/2)

    return velocity


i = Velocity(0.04)
print(i)