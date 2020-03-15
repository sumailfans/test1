
import numpy as np
import math
import matplotlib.pyplot as plt
x=np.arange(0,30,0.5)+0.5
y1=[math.log(a,1.3)+100 for a in x]
y2=[math.log(a,1.2)+100for a in x]
y3=[math.log(a,1.1)+100 for a in x]
plot1=plt.plot(x,y1,'-g',label="Maximizing Magnitude")
plot2=plt.plot(x,y2,'-r',label="Full dimensional ZF")
plot3=plt.plot(x,y3,'-b',label="Proposed Algorithm")
plt.legend(loc='lower right')
plt.grid(True)# 在坐标系上画格子
plt.xlabel("SNR(dB)")
plt.ylabel("Spectral efficiency(b/s/HZ)")
plt.show()





