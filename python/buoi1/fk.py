import math
l1 = 0.2
l2 = 0.15
theta1 = 0
theta2 = 90

r1 = math.radians(theta1)
r2 = math.radians (theta2)
x = l1*math.cos(r1) + l2*math.cos(r1+r2)
y = l1*math.sin(r1) + l2*math.sin(r1+r2)
print("x = ",x , "y = ", y)
print("goc khop 1: ",theta1, "goc khop 2: ", theta2)

