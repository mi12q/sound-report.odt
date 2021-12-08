import matplotlib.pyplot as plt
import numpy as np
import math

uglekis= [0, 0.01, 0.02, 0.03, 0.04, 0.05]
uglekis2 = [0, 1, 2, 3, 4, 5]

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

velocity = []
for i in uglekis:
    ms = xn2 * mn2 + xar * mar + xh20 * mh20 + i * mco2 + mo2 * (1-(i + xar + xh20 + xn2))

    gamma = (xn2 * mn2 * 3.5 + xar * mar * 2.5 + xh20 * mh20 * 4 + i * mco2 * 4.46 + mo2 * (1-(i + xar + xh20 + xn2)) * 3.5)/(xn2 * mn2 * 2.5 + xar * mar *1.5 + xh20 * mh20 * 3 + i * mco2 * 3.46 + mo2 * (1-( i + xar + xh20 + xn2 ))*2.5 )
    velocity.append((gamma*R*T/ms)**(1/2))

for i in velocity:
    print(i)

Va = 346.7
Vb = 342.6
V1=[]
V1.append(Va)
V1.append(Vb)
(k, b) = np.polyfit(uglekis2, velocity, 1)
x1 = (Va-b)/k
x2 = (Vb-b)/k
x = []
x.append(x1)
x.append(x2)
print(x1)
print(x2)
plt.title('Зависимость скорости звука от концентрации углекислого газа')
plt.plot(uglekis2,velocity, label = 'Аналитическая зависимость', color = 'orange')
plt.minorticks_on()
plt.xlabel("Концентрация CO2 [%]")
plt.ylabel("Скорость звука [м/с]")
plt.scatter(x1,Va, label = 'Значение в воздухе: 346.7 [м/с], -0.1 [%]')  
plt.scatter(x2,Vb, label = 'Значение в выдохе: 342.6 [м/с], 4 [%]')  
plt.grid(True, which = "minor", linestyle = "--", alpha = 1)
plt.legend()
plt.show()


