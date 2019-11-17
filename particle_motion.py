import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import numpy as np



#intial conditions


# ----------------------------------------------------
#set variable magnetic fields if necessary
def B(t,x,y,z):
    return [0,1,0]

def E(t,x,y,z):
    return [0,0,1]

# ----------------------------------------------------

v = [0,0,0]

tn = 0	#t_0
xn = 0	#x_0
yn = 0	#y_0
zn = 0	#z_0

xd = v[0]
yd = v[1]
zd = v[2]

Bx = B(tn,xn,yn,zn)[0]
By = B(tn,xn,yn,zn)[1]
Bz = B(tn,xn,yn,zn)[2]

Ex = E(tn,xn,yn,zn)[0]
Ey = E(tn,xn,yn,zn)[1]
Ez = E(tn,xn,yn,zn)[2]

vxb = [ yd*Bz - zd*By, zd*Bx - xd*Bz, xd*By - yd*Bx ]

q = 1


#euler's method
h = 0.001
tn = tn + h
xdn = xd + h*q*(Ex+yd*Bz - zd*By)
ydn = yd + h*q*(Ey+zd*Bx - xd*Bz)
zdn = zd + h*q*(Ez+xd*By - yd*Bx )




x = []
y = []
z = []

#append intial positions
x.append(xn)
y.append(yn)
z.append(zn)

xn = xn + h*xdn
yn = yn + h*ydn
zn = zn + h*zdn
#append positions calculated from initial velocity
x.append(xn)
y.append(yn)
z.append(zn)

tf = 30	#t_final
while tn <= tf:
    # finds B and E fields at location and time of particle then calculates the resulting motion due to this effect
	Bx = B(tn,xn,yn,zn)[0]
	By = B(tn,xn,yn,zn)[1]
	Bz = B(tn,xn,yn,zn)[2]
    
	Ex = E(tn,xn,yn,zn)[0]
	Ey = E(tn,xn,yn,zn)[1]
	Ez = E(tn,xn,yn,zn)[2]
	tn = tn + h
	xdn_new = xdn + h*q*(Ex+ydn*Bz - zdn*By)
	ydn_new = ydn + h*q*(Ey+zdn*Bx - xdn*Bz)
	zdn_new = zdn + h*q*(Ez+xdn*By - ydn*Bx )

	xn = xn + h*xdn_new
	yn = yn + h*ydn_new
	zn = zn + h*zdn_new

	xdn = xdn_new
	ydn = ydn_new
	zdn = zdn_new

	x.append(xn)
	y.append(yn)
	z.append(zn)
    
	#print(xn,yn,zn)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.title('particle motion')

plt.show()

plt.plot(x,y,'o', markersize = 0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

plt.plot(x,z,'o', markersize = 0.5)
plt.xlabel('x')
plt.ylabel('z')
plt.show()

plt.plot(y,z,'o', markersize = 0.5)
plt.xlabel('y')
plt.ylabel('z')
plt.show()
