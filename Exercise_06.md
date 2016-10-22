#第六次作业
##摘要
作业L1 2.10题强化版，考虑打击目标 高于或低于发射点的情况，并探究最小发射速度与打击目标之间的关系<br>
要求引入迎面风阻，考虑由海拔高度引起的空气密度变化对炮弹轨迹的影响，使用绝热模型进行计算。<br><br>
##背景
[上一次作业](https://github.com/toby459/compuational_physics_N2014301020139/blob/master/Exercise_05.md)尴尬的理解错了题目的意思，搞成了
海拔高度对g的影响，算了一遍之后发现并没有很大的差别，所以这次准备考虑风阻和空气密度的影响。<br><br>
##公式推导
首先，对于x，y，仍有<br><br>
![](http://latex.codecogs.com/gif.latex?x_%7Bi&plus;1%7D%3Dx_%7Bi%7D&plus;v_%7Bx%2Ci%7D%5CDelta%20t)<br>
![](http://latex.codecogs.com/gif.latex?v_%7Bx%2Ci&plus;1%7D%3Dv_%7Bx%2Ci%7D)<br><br>
而对于Vx和Vy，则有<br><br>
![](http://latex.codecogs.com/gif.latex?V_%7Bx%2Ci&plus;1%7D%3DV_%7Bx%2Ci%7D-%5Cfrac%7BF_%7Bx_%7Bdrag%7D%7D%7D%7Bm%7D%5CDelta%20t)<br>
![](http://latex.codecogs.com/gif.latex?V_%7By%2Ci&plus;1%7D%3DV_%7By%2Ci%7D-%5Cfrac%7BF_%7By_%7Bdrag%7D%7D%7D%7Bm%7D%5CDelta%20t-g%5CDelta%20t)<br><br>
由教材中的模型有，其中<br><br>
![](http://latex.codecogs.com/gif.latex?F_%7Bdrag%7D%3D%5Cfrac%7B%5Crho%20%7D%7B%5Crho_%7B0%7D%7D%5Cdot%7BF_%7Bdrag%7D%7D%3D%281-%5Cfrac%7Bay%7D%7BT_%7B0%7D%7D%29%5E%7B%5Calpha%7D%5Cdot%7BF_%7Bdrag%7D%7D)<br>
![](http://latex.codecogs.com/gif.latex?%5Cdot%7BF_%7Bdrag%2Cx/y%7D%7D%3D-B_%7B2%7Dvv_%7Bx/y%7D)<br><br>
综上所述，我们有<br><br>
![](https://github.com/toby459/compuational_physics_N2014301020139/blob/master/File_2/CP_ex06.PNG)<br>
此处g=9.8 m/s^2，B/m=4*10^-5 /m<br><br>
又因为题目要求改变目标的高度，故假设目标离发射点的水平距离为100km，上下两点高度差均为10km，以下是具体解决方法<br><br>
##结果表达
