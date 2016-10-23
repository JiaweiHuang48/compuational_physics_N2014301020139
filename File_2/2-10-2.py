# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 20:25:34 2016

@author: 黄佳玮
"""

import pylab as pl
import math
class  cannon:
    """
    Calculate the trajectory of the cannon shell including
    both air drag and the reduced air density at high altitudes.
    """
    def __init__(self,goal_x=20000,goal_y=100,time_step=0.05,X=0,Y=0,\
                 initial_speed=700,initial_angel=30,\
                 g=9.8,B=0.00004,a=0.0065,alpha=2.5,temperature_at_sea_level=288.15):
        self.theta=initial_angel
        self.Vx=[math.cos(self.theta*math.pi/180)*300]
        self.Vy=[math.sin(self.theta*math.pi/180)*300]
        self.X=[0]
        self.Y=[0]
        self.dt=time_step
        self.t=[0]
        self.g=g
        self.B=B
        self.a=a
        self.T=temperature_at_sea_level
        self.alpha=alpha
   def calculate(self):
        for i in range(21):
            v0 = 0
            angle = 25 + i*2 #25~65˚
            for j in range(20):
                dt = 0.1 
            while (self.x[-1]<=self.goal_x): 
                    if self.y[-1] > 46153.84615:
                        c = 0
                    else:    
            V=math.sqrt(math.pow(self.Vx[i],2)+math.pow(self.Vy[i],2))
            temp_X=self.X[i]+self.Vx[i]*self.dt
            temp_Y=self.Y[i]+self.Vy[i]*self.dt
            self.X.append(temp_X)
            self.Y.append(temp_Y)
            temp_Vx=self.Vx[i]-(1-self.Y[i]*self.a/self.T)**self.alpha*self.B*V*self.Vx[i]*self.dt
            temp_Vy=self.Vy[i]-self.g*self.dt-(1-self.Y[i]*self.a/self.T)**self.alpha*self.B*V*self.Vy[i]*self.dt
            self.Vx.append(temp_Vx)
            self.Vy.append(temp_Vy)
            self.t.append(self.t[i]+self.dt)
            i+=1
        r = (self.goal_x-self.x[-2])/(self.x[-1]-self.goal_x)
                self.y[-1] = (self.y[-2]+r*self.y[-1])/(r+1)
                self.x[-1] = self.goal_x
                if self.y[-1]>self.goal_y:
                    vt = self.v
                    self.v = v0+(vt-v0)/2
                if self.y[-1]<self.goal_y:
                    v0 = self.v0
                    self.v0 = v0+(vt-v0)/2
        self.v.append(self.v0)
        self.angle.append(angle)
        print (self.v,self.angle)
        vmin = min(self.v)
        l = self.v.index(vmin)
        amin = self.angle[l]
        print ('The minimum initial velocity:'+str(vmin)+'m/s')
        print('angle:'+str(amin)+'°')
a=cannon()
a.calculate()
