import pylab as pl
class uranium_decay:
   
    def __init__(self, number_of_nuclei_A = 100,number_of_nuclei_B = 0, time_constant = 1, time_of_duration = 5, time_step = 0.05):
        # unit of time is second
        self.nA_uranium = [number_of_nuclei_A]
        self.nB_uranium = [number_of_nuclei_B]
        self.t = [0]
        self.tau = time_constant
        self.dt = time_step
        self.time = time_of_duration
        self.nsteps = int(time_of_duration // time_step + 1)
        self.decayA=[-100]
        self.decayB=[100]
        print("Initial number of nuclei A ->", number_of_nuclei_A)
        print("Initial number of nuclei B ->", number_of_nuclei_B)
        print("Time constant ->", time_constant)
        print("time step -> ", time_step)
        print("total time -> ", time_of_duration)
    def calculate(self):
        for i in range(self.nsteps):
            tmp_A = self.nA_uranium[i] - self.nA_uranium[i] / self.tau * self.dt+self.nB_uranium[i] / self.tau * self.dt
            tmp_B = self.nB_uranium[i] - self.nB_uranium[i] / self.tau * self.dt+self.nA_uranium[i]/ self.tau * self.dt            
            changeA = -self.nA_uranium[i] / self.tau +self.nB_uranium[i] / self.tau
            changeB=  -self.nB_uranium[i] / self.tau +self.nA_uranium[i]/ self.tau
            self.nA_uranium.append(tmp_A)
            self.nB_uranium.append(tmp_B)
            self.decayA.append(changeA)
            self.decayB.append(changeB)
            self.t.append(self.t[i] + self.dt)
    def show_results(self):
        pl.subplot(211)
        plotA, = pl.plot(self.t, self.nA_uranium)
        plotB, = pl.plot(self.t, self.nB_uranium)        
        pl.xlabel('time ($s$)')
        pl.ylabel('Number of Nuclei')
        pl.subplot(212)
        plotA = pl.plot(self.t, self.decayA)
        plotB = pl.plot(self.t, self.decayB)
        pl.show()
        pl.xlabel('time ($s$)')
        pl.ylabel('dN/dt')
a = uranium_decay()
a.calculate()
a.show_results()
