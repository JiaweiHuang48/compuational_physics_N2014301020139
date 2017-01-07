fig = plt.figure()
ax = fig.add_subplot(1,1,1,xlim=(0,1),ylim=(-1,1))
line, = ax.plot([],[],lw=2)
def init(): 
    line.set_data([], []) 
    return line,


def animate(i):
 
    x = np.linspace(0,1,1001)
    y_now=copy(x)
    for d in range(1001):
        
        if 0<=d<=250:
            y_now[d]= 2*x[d]
        else:
            y_now[d]= -(2/3)*x[d]+2/3
    y_before =copy( y_now)
    y_after = np.zeros(1001)

    for j in range(i):
        for i in range(1001):
                if i== 0 or i== 1000:
                    y_after[i] = 0
                else:
                    y_after[i] =  y_now[i+1] - y_before[i] + y_now[i-1]

        y_before = copy(y_now)
        y_now = copy(y_after)
    y=y_now
    line.set_data(x,y)
    return line
