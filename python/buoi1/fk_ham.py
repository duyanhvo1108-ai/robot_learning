import math

l1 = float(input("nhap do dai khop 1: "))
l2 = float(input("\nnhap dp dao khop 2: "))

theta1 = float(input("\nnhap goc khop 1: "))
theta2 = float(input("\nnhap goc khop 2: "))


def fk(theta1,theta2):
	t1 = math.radians(theta1)
	t2 = math.radians(theta2)

	x = l1*math.cos(t1)+l2*math.cos(t1+t2)
	y = l1*math.sin(t1)+l2*math.sin(t1+t2)

	return x, y 

x,y = fk(theta1,theta2)

print("x = ",x, "y = ", y)
print("goc khop 1: ",theta1, "goc khop 2: ", theta2)

