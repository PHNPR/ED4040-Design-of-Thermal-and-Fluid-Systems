# Importing required Libraries
import math
import numpy as np
from sympy import solve , symbols , Eq
def sin(i) : return round(np.sin(np.radians(i)),6)
def cos(i) : return round(np.cos(np.radians(i)),6)

#Assumptions
vse = symbols('vse') 
vsc = vse
i = 0.6  
th , tc = 923 , 293 
vr = vce = vcc = i * vse
vh = vc = vr / 4
P = 500
f = 41.167
R = 8.3144
alpha = 90
R_He = R / 4 

#Calculations 
Vnet = vse + vsc + vcc + vce + vr + vh + vc
Mnet = ( Vnet / 22.4 ) * 4
temp1 = ( (vse/th)**2 + (vsc/tc)**2 + 2*vse*vsc*cos(alpha) / (th*tc) )**0.5 / 2
temp2 = vsc/(2*tc) + vcc/tc + vc/tc + vse/(2*th) + vcc/th + vh/th + vr * math.log(th/tc,10)/(th-tc)
temp = temp1 / temp2 
Pm = Mnet * R_He / ( temp2 * (1-temp**2)**0.5)
beta = np.degrees(math.atan((vse*sin(alpha)/th) / (vse*cos(alpha)/th + vsc/th )))

#Solving
W = P / f
Wc = -1 * math.pi * vsc * Pm * sin(beta) * ((1-temp**2)**0.5 - 1) / temp
We = -1 * math.pi * vse * Pm * sin(alpha-beta) * ((1-temp**2)**0.5-  1) / temp
equation = Eq(W , Wc + We)
sol = solve( equation , vse )
vse = round(abs(sol[0]),6)

print('The sweep volume during expansion is' , vse)

''' Calculating stroke and radius '''
st = symbols('stroke')
rad = st / 3
area = math.pi * (rad ** 2)
volume = area * st
equation = Eq(vse , volume)
sol = solve(equation , st)
st = round(abs(sol[0]),6)

print('The value of stroke length is' , st)
rad = st / 3
print('The value of radius is' , rad)
area = math.pi * (rad ** 2)
print('The value of Cross sectional area is' , rad)
rpm = f * 60
print('The value of RPM is' , int(rpm))
