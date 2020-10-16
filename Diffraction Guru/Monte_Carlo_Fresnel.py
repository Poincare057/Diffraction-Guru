import numpy as np
import math
import random
import matplotlib.pyplot as plt
#Rectangular aperture
xsize = 2
ysize = 4
pi = 3.1415926535
def E(x,y,z = 2,l = 0.000006):
    ''' field times other stuff to be integrated '''
    return complex(z*np.cos(2*pi*(x**2 + y**2 + z**2)**(0.5)), z*np.sin(2*pi*(x**2 + y**2 + z**2)**(0.5)))

def pattern(xsize = 0.003, ysize = 0.00003, z = 1, l = 0.000006):
    #Data
    V = xsize*ysize   #area
    n = 30              #number of points to sample at
    k = 30              #O(k^2) is number of points at which potential is calculated; k should be  for ease. 
    kstep = (xsize + ysize)/2         #Step size for above side lengths

    #Random Sampling
    montepoints = np.random.rand(n, 2)
    for i in range(n):
        montepoints[i][0] = montepoints[i][0]*xsize*0.5*(-1)**(random.randint(1, 4))
        montepoints[i][1] = montepoints[i][1]*ysize*0.5*(-1)**(random.randint(1,4))
    #print(montepoints)

    #Integration
    phi_real = np.zeros((k,k))   #np.zeros((z,y,x))
    phi_im = np.zeros((k,k))
    phi = np.zeros((k,k))
    for ity in range(k):
        for itx in range(k):
            f_real = 0
            f2_real = 0
            f_im = 0
            f2_im = 0
            r = [-k*kstep/2 + itx*kstep, -k*kstep/2 + ity*kstep]
            for monti in range(n):
                f_real += (E(r[0] - montepoints[monti][0], r[1] - montepoints[monti][1], z, l).real)/n
                f2_real += (E(r[0] - montepoints[monti][0], r[1] - montepoints[monti][1], z, l).real)**2 / n
                f_im += (E(r[0] - montepoints[monti][0], r[1] - montepoints[monti][1], z, l).imag)/ n
                f2_im += (E(r[0] - montepoints[monti][0], r[1] - montepoints[monti][1], z, l).imag)**2 / n
            phi_real[itx][ity] = V*f_real + ((-1)**random.randint(1, 10))*math.sqrt(abs(0.5*(f2_real - f_real**2)/n))
            phi_im[itx][ity] = V*f_im + ((-1)**random.randint(1,10))*math.sqrt(abs(0.5*(f2_im - f_im**2)/n))
            phi[itx][ity] = (phi_real[itx][ity]**2 + phi_im[itx][ity]**2)/(l**2)
    return np.transpose(phi)

##Monte Carlo Party ends here

