import pylab as pl
class cannon:
    def __init__(self, gravitational_constant=6.6*10**-11, mass_of_earth=6*10**24, radius_of_earth=6371000, time_step=0.1,\
                 total_time=40, initial_distance_x=0, initial_distance_y=0, initial_velocity_x=200, initial_velocity_y=200):
        self.vX = [initial_velocity_x]
        self.vY = [initial_velocity_y]
        self.x = [initial_distance_x]
        self.y = [initial_distance_y]
        self.t = [0]
        self.m = mass_of_earth
        self.g = gravitational_constant
        self.r = radius_of_earth
        self.dt = time_step
        self.time = total_time   
    def run(self):
        _time = 0
        while(_time < self.time):
            self.x.append(self.x[-1]+\
                          self.vX[-1] * self.dt)
            self.vY.append(self.vY[-1] -\
                          self.dt * self.g * self.m / (self.r + self.y[-1])**2)
            self.y.append(self.y[-1] +\
                          self.vY[-1] * self.dt)
            self.t.append(_time)
            _time += self.dt    
    def show_results(self):
        font = {'family': 'serif',
                'color':  'darkred',
                'weight': 'normal',
                'size': 16,
        }
        pl.plot(self.x, self.y)
        pl.title('Trajectory of cannon shell', fontdict = font)
        pl.xlabel('x ($m$)')
        pl.ylabel('y ($m$)')
        pl.show()
a = cannon()
a.run()
a.show_results()
