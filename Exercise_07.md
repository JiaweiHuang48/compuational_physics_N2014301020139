#第7次作业
Exercise 3.12<br>
In constructing the Poincaré section in Figure 3.9 we plotted points only at times that were in phase with the drive force; that is,
at times t=2πn/Ωd , where n is an integer. At these values of t the driving force passed through zero [see(3.18)]. However, we could jusi as 
easily have chosen to make the plot at times corresponding to a maximum of the drive force, 
or at times π/4 out-of-phase with this force, etc. Construct the Poincaré sections for these cases and compare them with Figure 3.9.
Exercise 3.13<br>
Write a program to calculate and compare the behavior of two, nearly identical pendulums. Use it to calculate the divergence of two 
nearby trajectories in the chaotic regime, as in Figure 3.7, and make a qualitative estimate of the corresponding Lyapunov exponent 
from the slope of a plot of log(Δθ) as a function of t .
Exercise 3.14<br>
Repeat the previous problem, but give the two pendulums slightly different damping factors. How does the value of the Lyapunov exponent 
compare with that found in Figure 3.7?

##摘要
本次作业通过Euler-Cromer方法模拟计算在考虑各种因素的情况下的单摆运动，并讨论其引起的混沌现象。

##背景
混沌现象是指发生在确定性系统中的貌似随机的不规则运动，一个确定性理论描述的系统，其行为却表现为不确定性一不可重复、不可预测，这就是混沌现象。进一步研究表明，
混沌是非线性动力系统的固有特性，是非线性系统普遍存在的现象。牛顿确定性理论能够充分处理的多为线性系统，而线性系统大多是由非线性系统简化来的。

##内容
考虑阻尼、非线性和驱动力时的单摆运动方程：<br> 
<br>
![]()<br>
<br>
推出： <br>
<br>
![]()<br>
<br>
带入Euler-Cromer method进行模拟运算：<br> 
<br>
![]()<br>
<br>
如果θ超过[-π,π]那么其值加上或减去π,使其值依然在[-π,π]内。<br>
除了特殊情况外各参数数值如下：<br>
<br>
![]()<br>
<br>
##结果
3.12<br>
![代码1]()<br>
![]()<br>
![]()<br>
![]()<br>
3.13&3.14<br>
![代码二]()<br>
![]()<br>
![]()<br>
![]()<br>
<br>
##总结
我们通过Euler-Cromer 方法初步演示了混沌现象，即有确定算法的情况下，得到不确定的结果。
