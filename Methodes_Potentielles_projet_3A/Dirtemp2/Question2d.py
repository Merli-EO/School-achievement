import matplotlib.pyplot  as plt
import numpy as np



Data11 = np.loadtxt("set2_no_0.5resist.txt")
Data12 = np.loadtxt("set2_no_0.5thick.txt")
Data13 = np.loadtxt("set2_no_2resist.txt")
Data14 = np.loadtxt('set2_no_2thick.txt')
Data15 = np.loadtxt('set2_output_model1_258879614.txt')

Data21 = np.loadtxt("set2_with_0.5resist.txt")
Data22 = np.loadtxt("set2_with_0.5thick.txt")
Data23 =  np.loadtxt("set2_with_2resist.txt")
Data24 = np.loadtxt('set2_with_2thick.txt')
Data25 = np.loadtxt('set2_output_model2_258879614.txt')

Max1 = len(Data11)
RangeCross = [ Data11[i][0] for i in range(Max1) ]      #Range Cross

Inline_E_amp11 = [ Data11[i][3] for i in range(Max1) ]  
Inline_E_phase11 = [ Data11[i][4] for i in range(Max1) ]  
Inline_E_amp21 = [ Data21[i][3] for i in range(Max1) ]  
Inline_E_phase21 = [ Data21[i][4] for i in range(Max1) ]  

Inline_E_amp12 = [ Data12[i][3] for i in range(Max1) ]  
Inline_E_phase12 = [ Data12[i][4] for i in range(Max1) ]  
Inline_E_amp22 = [ Data22[i][3] for i in range(Max1) ]  
Inline_E_phase22 = [ Data22[i][4] for i in range(Max1) ] 

Inline_E_amp13 = [ Data13[i][3] for i in range(Max1) ]  
Inline_E_phase13 = [ Data13[i][4] for i in range(Max1) ]  
Inline_E_amp23 = [ Data23[i][3] for i in range(Max1) ]  
Inline_E_phase23 = [ Data23[i][4] for i in range(Max1) ] 

Inline_E_amp14 = [ Data14[i][3] for i in range(Max1) ]  
Inline_E_phase14 = [ Data14[i][4] for i in range(Max1) ]  
Inline_E_amp24 = [ Data24[i][3] for i in range(Max1) ]  
Inline_E_phase24 = [ Data24[i][4] for i in range(Max1) ] 


Inline_E_amp15 = [ Data15[i][3] for i in range(Max1) ]  
Inline_E_phase15 = [ Data15[i][4] for i in range(Max1) ]  
Inline_E_amp25 = [ Data25[i][3] for i in range(Max1) ]  
Inline_E_phase25 = [ Data25[i][4] for i in range(Max1) ] 

fontTitle = {'family': 'serif', 'color':  'darkblue','weight': 'bold','size': 16 }
font = {'family': 'monospace', 'color':  'darkblue','weight': 'light','size': 12 }


fig, (ax, ax1) = plt.subplots( nrows=1, ncols=2, sharex=True,figsize=(12, 6))

ax.set_xlim(0,15000)
ax.set_xlabel('Range (m)', fontdict=font)
ax.set_ylabel('Amplitude', fontdict=font)
ax.set_title('Inline E Amplitude', fontdict=fontTitle)
ax.set_yscale('log')
ax.plot(RangeCross, Inline_E_amp11, 'darkgreen', label=r'model1 $\rho$=$\rho$/2 ')
ax.plot(RangeCross, Inline_E_amp21, 'b3', label=r'model2 $\rho$=$\rho$/2')
ax.plot(RangeCross, Inline_E_amp12, 'lightblue', label='model1 h=h/2')
ax.plot(RangeCross, Inline_E_amp22, 'g2', label='model2 h=h/2')
ax.plot(RangeCross, Inline_E_amp13, 'lightgreen', label=r'model1 $\rho$=2$\rho$')
ax.plot(RangeCross, Inline_E_amp23, 'k1', label=r'model2 $\rho$=2$\rho$')
ax.plot(RangeCross, Inline_E_amp14, 'red', label='model1 h=2h')
ax.plot(RangeCross, Inline_E_amp24, 'yx', label='model2 h=2h')
ax.plot(RangeCross, Inline_E_amp15, 'darkblue', label='model1 original ')
ax.plot(RangeCross, Inline_E_amp25, 'r*', label='model2 original')
ax.tick_params(labelcolor='tab:orange')
ax.legend()
ax.grid()

ax1.set_xlim(0,15000)
ax1.set_xlabel('Range (m)', fontdict=font)
ax1.set_ylabel('Phase', fontdict=font)
ax1.set_title('Inline E Phase', fontdict=fontTitle)
ax1.plot(RangeCross,Inline_E_phase11, 'darkgreen', label=r'model1 $\rho$=$\rho$/2 ')
ax1.plot(RangeCross,Inline_E_phase21, 'b3', label=r'model2 $\rho$=$\rho$/2 ')
ax1.plot(RangeCross,Inline_E_phase12, 'lightblue', label='model1 h=h/2')
ax1.plot(RangeCross,Inline_E_phase22, 'g2', label='model2 h=h/2')
ax1.plot(RangeCross,Inline_E_phase13, 'lightgreen', label=r'model1 $\rho$=2$\rho$ ')
ax1.plot(RangeCross,Inline_E_phase23, 'k1', label=r'model1 $\rho$=$\rho$/2 ')
ax1.plot(RangeCross,Inline_E_phase14, 'red', label='model1 h=2h')
ax1.plot(RangeCross,Inline_E_phase24, 'yx', label='model2 h=2h')
ax1.plot(RangeCross,Inline_E_phase15, 'darkblue', label='model1 original')
ax1.plot(RangeCross,Inline_E_phase25, 'r+', label='model2 original')
ax1.tick_params(labelcolor='tab:orange')
ax1.legend()
ax1.grid()


fig.set_facecolor('#eafff5')
plt. tight_layout()
plt.show()
fig.savefig('Question2d_plot.png')


