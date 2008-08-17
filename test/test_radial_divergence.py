from xfab import tools,detector
import numpy as n
#
# Parameters describing experimental setup 
#

distance = 61.977       
dety_center = 1023.5
detz_center = 1023.5
y_size = 0.04677648  
z_size = 0.04808150  
dety_size = 2048.0   
detz_size = 2048.0
tilt_x = 0.0
tilt_y = 0.0
tilt_z = 0.0
wedge = 0.0
unit_cell = [4.04975, 4.04975, 4.04975, 90, 90, 90]
sgno = 225
U = n.array([-0.52880000,  0.78460000,  0.32380000, -0.51780000,  0.00400000, -0.85550000, -0.67250000, -0.62000000,  0.40410000]).reshape(3,3)
pos = [0.0, 0.0 , 0.0]


hkl = [1,1,1]

unit_cell = [4.04975, 4.04975, 4.04975, 90, 90, 90]
B = tools.FormB(unit_cell)
Gc = n.dot(B,hkl)
Gw = n.dot(U,Gc)



wavelength_0 = 0.4859292
wavelength = wavelength_0 
tth = tools.tth2(Gw,wavelength)
(Omega, Eta) = tools.find_omega_wedge(Gw,tth,wedge)
Om = tools.OMEGA(Omega[1])
Gt = n.dot(Om,Gw)

(dety,detz) = detector.det_coor(Gt,n.cos(tth),wavelength,distance,y_size,z_size,dety_center,detz_center,n.identity(3),0,0,0)

wavelength = wavelength_0*(1.0+1e-3)
#wavelength = wavelength_0*(1.0+.1e-1)
tth = tools.tth2(Gw,wavelength)
(Omega, Eta) = tools.find_omega_wedge(Gw,tth,wedge)
Om = tools.OMEGA(Omega[1])
Gt = n.dot(Om,Gw)

(ddety,ddetz) = detector.det_coor(Gt,n.cos(tth),wavelength,distance,y_size,z_size,dety_center,detz_center,n.identity(3),0,0,0)

### CHANGE UNIT_CELL
unit_cell = n.array([4.04975, 4.04975, 4.04975, 90, 90, 90])
unit_cell[:3] =  unit_cell[:3]*(1.0+1.0e-3)
B = tools.FormB(unit_cell)
Gc = n.dot(B,hkl)
Gw = n.dot(U,Gc)

wavelength = wavelength_0
tth = tools.tth2(Gw,wavelength)
(Omega, Eta) = tools.find_omega_wedge(Gw,tth,wedge)
Om = tools.OMEGA(Omega[1])
Gt = n.dot(Om,Gw)

(dddety,dddetz) = detector.det_coor(Gt,n.cos(tth),wavelength,distance,y_size,z_size,dety_center,detz_center,n.identity(3),0,0,0)



#### Playing with an algo for convolute the radial spread of the reflections
from polyxsim import pixel_trace
from scipy.stats import norm

pixels =  pixel_trace.pixel_trace([996,995,1005,1007])
pixels2 = n.array([[0,0,0,0.0]])

path_total = pixels[:,2].sum()

t_old = norm.cdf(ZZZZ)
frac = n.zeros(len(pixels))
for i in range(len(pixels)):
    t_new = norm.cdf(pixel[i,2])
    frac[i] = t_new-t_old
    t_old = t_new

pixels2 = n.concatenate(([[0,0,0.0]],pixels))
cums = pixels2[:,2].cumsum()
cdfcums = norm.cdf(cums-cums[-1]/2.0)
frac =  cdfcums[1:]-cdfcums[:-1]
