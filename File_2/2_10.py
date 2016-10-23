import pylab as pl
import math
class  cannon:

    def __init__(self,time_step=0.05,X=0,Y=0,initial_speed=700,initial_angel=30,g=9.8,B=0.00004,a=0.0065,alpha=2.5,temperature_at_sea_level=288.15):
        self.theta=initial_angel
        self.Vx=[math.cos(self.theta*math.pi/180)*700]
        self.Vy=[math.sin(self.theta*math.pi/180)*700]
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
        i=0
        while self.Y[i]>=0:                  
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
    def show_result(self):      
        pl.plot(self.X,self.Y)
        pl.xlabel("X(m)")
        pl.ylabel("Y(m)")
        pl.xlim(0,30000)
        pl.ylim(0,20000)
        pl.show()
    def landing_point(self):         
       self.angel_point=dict()
       self.angel_point[self.theta]=self.X[-1]-self.Y[-1]*(self.X[-1]-self.X[-2])/(self.Y[-1]-self.Y[-2])
       print(self.angel_point)
a=cannon()    
a.calculate()
a.show_result() 
a.landing_point() 

class Maximum_of_range(cannon): 
     def line_of_different_angel(self): 
         self.theta=0
         for i in range(91):
             b=cannon(initial_angel=self.theta) 
             b.calculate()
             b.show_result()
             b.landing_point()
             self.theta=self.theta+1
b=Maximum_of_range()
b.line_of_different_angel()
