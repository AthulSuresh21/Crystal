

#----------------------------------------------------------------#
#			AUTHOR: ATHUL SURESH			 #
#----------------------------------------------------------------#

#program to calculate the angle between a given vector and the crystallographic axes

from math import*
#getting the unit cell information

a=float(input('Enter a')) #cell_dimensions_lengths
b=float(input('Enter b')) #cell_dimensions_lengths
c=float(input('Enter c')) #cell_dimensions_lengths
u=float(input('Enter alpha')) #cell_dimensions_angles
v=float(input('Enter beta')) #cell_dimensions_angles
w=float(input('Enter gamma')) #cell_dimensions_angles
#converting to radians
u=u*(pi/180.0)
v=v*(pi/180.0)
w=w*(pi/180.0)
V=a*b*c*(1-cos(u)**2-cos(v)**2-cos(w)**2+2*cos(u)*cos(v)*cos(w))**0.5
print("Volume of unit cell=", V)
#Calculating the matrix elements of M matrix

m11=a**-1
m12=-(cos(w)/sin(w))/a
m13=((b*cos(w)*c*(cos(u)-cos(v)*cos(w))-b*c*cos(v)*(sin(w))**2.0))/(sin(w)*V)

m21=0.0
m22=1.0/(b*sin(w))
m23=-(a*c*(cos(u)-cos(v)*cos(w)))/(sin(w)*V)

m31=0.0
m32=0.0
m33=(a*b*sin(w))/V

A=[m11,m12,m13]
B=[m21,m22,m23]
C=[m31,m32,m33]

print('A=',A)
print('B=',B)
print('C=',C)

#Getting the coordinates of the cenroid

print('Enter the position vector of the centroid')

x=float(input('Enter x'))
y=float(input('Enter y'))
z=float(input('Enter z'))

R=[x,y,z]

#calculating the norms

norm_R=(x**2+y**2+z**2)**0.5
norm_A=(m11**2+m12**2+m13**2)**0.5
norm_B=(m21**2+m22**2+m23**2)**0.5
norm_C=(m31**2+m32**2+m33**2)**0.5

#calculating the cosines

cs_AR=abs((x*m11+y*m12+z*m13)/((norm_R)*(norm_A)))
cs_BR=abs((x*m21+y*m22+z*m23)/((norm_R)*(norm_B)))
cs_CR=abs((x*m31+y*m32+z*m33)/((norm_R)*(norm_C)))

thetA=(180.0/pi)*acos(cs_AR)
thetB=(180.0/pi)*acos(cs_BR)
thetC=(180.0/pi)*acos(cs_CR)

Theta=[thetA,thetB,thetC]

print('Angles with respect to a,b and c axes respectively are',Theta)

