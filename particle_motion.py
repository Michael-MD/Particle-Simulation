import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

#intial conditions

v = [0,0,0]
B = [1,0,0]

xd = v[0]
yd = v[1]
zd = v[2]

Bx = B[0]
By = B[1]
Bz = B[2]

E = [0,0,1]
Ex = E[0]
Ey = E[1]
Ez = E[2]

vxb = [ yd*Bz - zd*By, zd*Bx - xd*Bz, xd*By - yd*Bx ]

q = 1
F = q*(E+vxb)

xdd = F[0]
ydd = F[1]
zdd = F[2]

tn = 0	#t_0
xn = 0	#x_0
yn = 0	#y_0
zn = 0	#z_0

#euler's method
h = 0.001
tn = tn + h
xdn = xd + h*q*(Ex+yd*Bz - zd*By)
ydn = yd + h*q*(Ey+zd*Bx - xd*Bz)
zdn = zd + h*q*(Ez+xd*By - yd*Bx )

xn = xn + h*xdn
yn = yn + h*ydn
zn = zn + h*zdn

x = []
y = []
z = []
tf = 30	#t_final
while tn <= tf:
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