import matplotlib.pyplot  as plt
import numpy as np



Data10025 = np.loadtxt("set1_output_no_0.025hz_1279208487.txt")
Data105 = np.loadtxt("set1_output_no_0.5hz_862791467.txt")
Data11 =  np.loadtxt("set1_output_no_1hz_94924870.txt")
Data125 = np.loadtxt('set1_output_model1_258879614.txt')

Data20025 = np.loadtxt("set1_output_with_0.025hz_1279208487.txt")
Data205 = np.loadtxt("set1_output_with_0.5hz_862791467.txt")
Data21 =  np.loadtxt("set1_output_with_1hz_94924870.txt")
Data225 = np.loadtxt('set1_output_model2_258879614.txt')

Max1 = len(Data11)
RangeCross = [ Data11[i][0] for i in range(Max1) ]      #Range Cross

Inline_E_amp0025 = [ Data10025[i][1] for i in range(Max1) ]  
Inline_E_phase0025 = [ Data10025[i][2] for i in range(Max1) ]  
Inline_E_amp20025 = [ Data20025[i][1] for i in range(Max1) ]  
Inline_E_phase20025 = [ Data20025[i][2] for i in range(Max1) ]  

Inline_E_amp05 = [ Data105[i][1] for i in range(Max1) ]  
Inline_E_phase05 = [ Data105[i][2] for i in range(Max1) ]  
Inline_E_amp205 = [ Data205[i][1] for i in range(Max1) ]  
Inline_E_phase205 = [ Data205[i][2] for i in range(Max1) ] 

Inline_E_amp1 = [ Data11[i][1] for i in range(Max1) ]  
Inline_E_phase1 = [ Data11[i][2] for i in range(Max1) ]  
Inline_E_amp21 = [ Data21[i][1] for i in range(Max1) ]  
Inline_E_phase21 = [ Data21[i][2] for i in range(Max1) ] 

Inline_E_amp25 = [ Data125[i][1] for i in range(Max1) ]  
Inline_E_phase25 = [ Data125[i][2] for i in range(Max1) ]  
Inline_E_amp225 = [ Data225[i][1] for i in range(Max1) ]  
Inline_E_phase225 = [ Data225[i][2] for i in range(Max1) ] 


fontTitle = {'family': 'serif', 'color':  'darkblue','weight': 'bold','size': 16 }
font = {'family': 'monospace', 'color':  'darkblue','weight': 'light','size': 12 }


fig, (ax, ax1) = plt.subplots( nrows=1, ncols=2, sharex=True,figsize=(12, 6))

ax.set_xlim(0,15000)
ax.set_xlabel('Range (m)', fontdict=font)
ax.set_ylabel('Amplitude', fontdict=font)
ax.set_title('Crossline E Amplitude', fontdict=fontTitle)
ax.set_yscale('log')
ax.plot(RangeCross, Inline_E_amp0025, 'darkgreen', label='model1 f=0.025Hz')
ax.plot(RangeCross, Inline_E_amp20025, 'b3', label='model2 f=0.025Hz')
ax.plot(RangeCross, Inline_E_amp05, 'lightblue', label='model1 f =0.5Hz')
ax.plot(RangeCross, Inline_E_amp205, 'g2', label='model2 f=0.5Hz')
ax.plot(RangeCross, Inline_E_amp1, 'lightgreen', label='model1 f=1Hz')
ax.plot(RangeCross, Inline_E_amp21, 'k1', label='model2 f=1Hz')
ax.plot(RangeCross, Inline_E_amp25, 'darkblue', label='model1 f=0.25Hz')
ax.plot(RangeCross, Inline_E_amp225, 'r*', label='model2 f=0.25')
ax.tick_params(labelcolor='tab:orange')
ax.legend()
ax.grid()

ax1.set_xlim(0,15000)
ax1.set_xlabel('Range (m)', fontdict=font)
ax1.set_ylabel('Phase', fontdict=font)
ax1.set_title('Crossline E Phase', fontdict=fontTitle)
ax1.plot(RangeCross,Inline_E_phase0025, 'darkgreen', label='model1 f=0.025Hz')
ax1.plot(RangeCross,Inline_E_phase20025, 'b3', label='model2 f=0.025Hz')
ax1.plot(RangeCross,Inline_E_phase05, 'lightblue', label='model1 f=0.5')
ax1.plot(RangeCross,Inline_E_phase205, 'g2', label='model2 f=0.5Hz')
ax1.plot(RangeCross,Inline_E_phase1, 'lightgreen', label='model1 f=1Hz')
ax1.plot(RangeCross,Inline_E_phase21, 'k1', label='model2 f=1Hz')
ax1.plot(RangeCross,Inline_E_phase25, 'darkblue', label='model1 f=0.25Hz')
ax1.plot(RangeCross,Inline_E_phase225, 'r+', label='model2 f=0.25Hz')
ax1.tick_params(labelcolor='tab:orange')
ax1.legend()
ax1.grid()


fig.set_facecolor('#eafff5')
plt. tight_layout()
plt.show()
fig.savefig('Question2a_plot.png')


