import math
l1 = 0.2
l2 = 0.15
def fk(theta1,theta2):
	t1 = math.radians(theta1)
	t2 = math.radians(theta2)
	x = l1*math.cos(t1)+l2*math.cos(t1+t2)
	y = l1*math.sin(t1)+l2*math.sin(t1+t2)
	return x,y

theta2 = 45
for g in range(0,91,15):
	theta1 = g
	x,y = fk(theta1,theta2)
	print(f"gia tri x: {x:.3f} gia tri y: {y:.3f} ")
	print("\nGoc theta1: ",theta1,"Goc theta2:  ",theta2)
 
