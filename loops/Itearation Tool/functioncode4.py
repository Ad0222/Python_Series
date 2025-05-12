import math

def circle_stats(radius):
    area=math.pi*radius**2
    circumference=2*math.pi**radius
    value=round(area,3)
    value1=round(circumference,3)
    return value,value1
a,c=circle_stats(3)

print("Area:",a,"circumference:",c)