import matplotlib.pyplot  as plt
import numpy as np



Data5000 = np.loadtxt("set1_no_5000.txt")
Data10000= np.loadtxt("set1_no_10000.txt")
Data15000 = np.loadtxt('set1_output_model1_258879614.txt')

Data25000 = np.loadtxt("set1_with_5000.txt")
Data210000 = np.loadtxt("set1_with_10000.txt")
Data215000 = np.loadtxt('set1_output_model2_258879614.txt')

Max1 = len(Data5000)


RangeCross = [ Data5000[i][0] for i in range(Max1) ]      #Range Cross
Inline_E_amp0025 = [ Data5000[i][1] for i in range(Max1) ]  
Inline_E_phase0025 = [ Data5000[i][2] for i in range(Max1) ]  
Inline_E_amp20025 = [ Data25000[i][1] for i in range(Max1) ]  
Inline_E_phase20025 = [ Data25000[i][2] for i in range(Max1) ]  

RangeCross2 = [ Data10000[i][0] for i in range(Max1) ] 
Inline_E_amp05 = [ Data10000[i][1] for i in range(Max1) ]  
Inline_E_phase05 = [ Data10000[i][2] for i in range(Max1) ]  
Inline_E_amp205 = [ Data210000[i][1] for i in range(Max1) ]  
Inline_E_phase205 = [ Data210000[i][2] for i in range(Max1) ] 

RangeCross3 = [ Data15000[i][0] for i in range(Max1) ] 
Inline_E_amp1 = [ Data15000[i][1] for i in range(Max1) ]  
Inline_E_phase1 = [ Data15000[i][2] for i in range(Max1) ]  
Inline_E_amp21 = [ Data215000[i][1] for i in range(Max1) ]  
Inline_E_phase21 = [ Data215000[i][2] for i in range(Max1) ] 



fontTitle = {'family': 'serif', 'color':  'darkblue','weight': 'bold','size': 16 }
font = {'family': 'monospace', 'color':  'darkblue','weight': 'light','size': 12 }


fig, ( (ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots( nrows=3, ncols=2, sharex=False ,figsize=(12, 6))


ax1.set_xlim(0,10000)
ax1.set_xlabel('Range (m)', fontdict=font)
ax1.set_ylabel('Amplitude', fontdict=font)
ax1.set_title('Crossline E Amplitude', fontdict=fontTitle)
ax1.set_yscale('log')
ax1.plot(RangeCross2, Inline_E_amp05, 'lightblue', label='model1 offset =10km')
ax1.plot(RangeCross2, Inline_E_amp205, 'g2', label='model2 offset=10km')
ax1.tick_params(labelcolor='tab:orange')
ax1.legend()
ax1.grid()

ax2.set_xlim(0,10000)
ax2.set_xlabel('Range (m)', fontdict=font)
ax2.set_ylabel('Phase', fontdict=font)
ax2.set_title('Crossline E Phase', fontdict=fontTitle)
ax2.plot(RangeCross2,Inline_E_phase05, 'lightblue', label='model1 f=0.5')
ax2.plot(RangeCross2,Inline_E_phase205, 'g2', label='model2 f=0.5Hz')
ax2.tick_params(labelcolor='tab:orange')
ax2.legend()
ax2.grid()

ax3.set_xlim(0,15000)
ax3.set_xlabel('Range (m)', fontdict=font)
ax3.set_ylabel('Amplitude', fontdict=font)
ax3.set_title('Crossline E Amplitude', fontdict=fontTitle)
ax3.set_yscale('log')
ax3.plot(RangeCross3, Inline_E_amp1, 'lightgreen', label='model1 offset=15km')
ax3.plot(RangeCross3, Inline_E_amp21, 'k1', label='model2 offset=15km')
ax3.tick_params(labelcolor='tab:orange')
ax3.legend()
ax3.grid()

ax4.set_xlim(0,15000)
ax4.set_xlabel('Range (m)', fontdict=font)
ax4.set_ylabel('Phase', fontdict=font)
ax4.set_title('Crossline E Phase', fontdict=fontTitle)
ax4.plot(RangeCross3,Inline_E_phase1, 'lightgreen', label='model1 offset=15km')
ax4.plot(RangeCross3,Inline_E_phase21, 'k1', label='model2 offset=15km')
ax4.tick_params(labelcolor='tab:orange')
ax4.legend()
ax4.grid()


ax5.set_xlim(0,5000)
ax5.set_xlabel('Range (m)', fontdict=font)
ax5.set_ylabel('Amplitude', fontdict=font)
ax5.set_title('Crossline E Amplitude', fontdict=fontTitle)
ax5.set_yscale('log')
ax5.plot(RangeCross, Inline_E_amp0025, 'darkblue', label='model1 offset=5km')
ax5.plot(RangeCross, Inline_E_amp20025, 'r*', label='model2 offset=5km')
ax5.tick_params(labelcolor='tab:orange')
ax5.legend()
ax5.grid()

ax6.set_xlim(0,5000)
ax6.set_xlabel('Range (m)', fontdict=font)
ax6.set_ylabel('Phase', fontdict=font)
ax6.set_title('Crossline E Phase', fontdict=fontTitle)
ax6.plot(RangeCross,Inline_E_phase0025, 'darkblue', label='offset=5km')
ax6.plot(RangeCross,Inline_E_phase20025, 'r+', label='offset=5km')
ax6.tick_params(labelcolor='tab:orange')
ax6.legend()
ax6.grid()

fig.set_facecolor('#eafff5')
plt. tight_layout()
plt.show()
fig.savefig('Question2c_plot.png')





