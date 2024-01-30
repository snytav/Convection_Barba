import numpy as np

from convection_basic import linear_convection_solve
import numpy
import matplotlib.pyplot as plt
from matplotlib import pyplot, cm

Lx = 2



nx = 41  # try changing this number from 41 to 81 and Run All ... what happens?
dx = 2 / (nx-1)
nt = 5    #nt is the number of timesteps we want to calculate
dt = .025  #dt is the amount of time each timestep covers (delta t)
c = 1      #assume wavespeed of c = 1
Lt = dt*nt
u = numpy.zeros(nx)      #numpy function ones()
# u[int(.5 / dx):int(1 / dx + 1)] = 2  #setting u = 2 between 0.5 and 1 as per our I.C.s
x = np.linspace(0,1,int(nx/2))
u[:int(nx/2)] = np.sin(np.pi*x)

from surface import draw_surf

u,u2D = linear_convection_solve(u,c,dx,dt,Lx, nx, Lt, nt)

draw_surf(Lx,nx,Lt,nt,u2D) #(u,c,dx,dt,Lx, nx, Lt, nt)

qq = 0