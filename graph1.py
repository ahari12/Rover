import matplotlib.pyplot as plt
from math import pi,sqrt
import math
n=2
print("first point is  at origin already given enter %d node",n-1)
#input x points of the nodes
x=[float(input("enter the x value")) for i in range(0,n-1)]
x.insert(0,0)
#input y points of the nodes
y=[float(input("enter the y value"))for i in range(0,n-1)]
y.insert(0,0)
for i in range(0,n-1):
    a=y[i+1]
    #refrence line for angle
    x1=[x[i],x[i]]
    y1=[y[i],a]
    #distance of the line joining node
    distance=sqrt(((x[i+1]-x[i])**2)+((y[i+1]-y[i])**2))
    #distance of the reference line
    dis2=sqrt(((x1[1]-x1[0])**2)+((y1[1]-y1[0])**2))
    #angle formula
    angle=math.acos(dis2/distance)
    angle1=angle*(180/pi)
    if(x[i]>x[i+1]):

        
        if(y[i]>y[i+1]):

            print("distance",distance)
            print("angle",-angle1+90)
        else:
            
            print("distance",distance)
            
            print("angle360",-angle1)
    else:

        if(y[i]>y[i+1]):
                 print("distance ", distance)
                 print("angle",angle1+90)
        else:
            print("distance",distance)
            print("angle",angle1)
plt.plot(x,y)
plt.plot(x1,y1)
plt.plot(x,y,'o')
plt.show()