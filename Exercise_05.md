#第五次作业
##课后习题2.8
In our model of the cannon shell trajectory we assumed that the acceleration due to gravity, g, is a constant. It will, of cuorse, depend on altitude. Add thie to rhe model and calculate how much it affects the range.
##摘要
考虑炮弹在飞行的过程中重力加速度随炮弹的高度而变化，在表达式中加入重力加速度g随海拔高度y变化的式子   ![](http://latex.codecogs.com/gif.latex?g%3D%5Cfrac%7BGM%7D%7B%28R&plus;y%29%5E%7B2%7D%7D)<br>
详见后面的推导
##公式推导
当不考虑空气阻力等其他因素，只考虑重力加速度变化时，炮弹运动轨迹方程：<br>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bdx%7D%7Bdt%7D%3Dv_%7Bx%7D)<br>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bdv_%7Bx%7D%7D%7Bdt%7D%3D0)<br>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bdy%7D%7Bdt%7D%3Dv_%7By%7D)<br>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bdv_%7By%7D%7D%7Bdt%7D%3D-%5Cfrac%7BGM%7D%7B%28R&plus;y%5E%7B2%7D%29%7D)<br><br>
解得<br>
![](http://latex.codecogs.com/gif.latex?x_%7Bi&plus;1%7D%3Dx_%7Bi%7D&plus;v_%7Bx%2Ci%7D%5CDelta%20t)<br>
![](http://latex.codecogs.com/gif.latex?v_%7Bx%2Ci&plus;1%7D%3Dv_%7Bx%2Ci%7D)<br>
![](http://latex.codecogs.com/gif.latex?y_%7Bi&plus;1%7D%3Dy_%7Bi%7D&plus;v_%7By%2Ci%7D%5CDelta%20t)<br>
![](http://latex.codecogs.com/gif.latex?v_%7By%2Ci&plus;1%7D%3Dv_%7By%2Ci%7D-%5Cfrac%7BGM%7D%7B%28R&plus;y%29%5E%7B2%7D%7D%5CDelta%20t)<br>
##结果表达
###[代码链接（考虑y对g的影响）](https://github.com/toby459/compuational_physics_N2014301020139/blob/master/File_2/Exercise_05_code.py)<br>
###[代码链接（不考虑y对g的影响）](https://github.com/toby459/compuational_physics_N2014301020139/blob/master/File_2/Exercise_05_code2.py)<br>
###图像<br>
考虑y对g的影响：<br>
![](https://github.com/toby459/compuational_physics_N2014301020139/blob/master/File_2/EXercise_05截图.PNG)<br>
不考虑y对g的影响：<br>
![](https://github.com/toby459/compuational_physics_N2014301020139/blob/master/File_2/EXercise_05截图2.PNG)<br>
##总结
两张图粗略看上去差不多，但仔细对比起来还是有不同，可见y对g还是有一定影响，但是当y比较小时，影响并不大。<br>
另外，不知道怎么把两条曲线弄到一张图上去，大半夜的也不好问，搞清楚了下次再来<br>
最后感谢蔡老师的屁屁踢，还有不留名的前辈留下的用 codecogs写公式的办法，吼吼用~
