import matplotlib.pyplot  as plt
import numpy as np

Data1 = np.loadtxt("2ièmeSet.txt")
Data12 = np.loadtxt("2ièmeSet.txt")
Data3 = np.loadtxt("set1_model1")

Max1 = len(Data1)
RangeCross = [ Data1[i][0] for i in range(Max1) ]      #Range Cross
Crossline_B_amp = [ Data1[i][1] for i in range(Max1) ]
Crossline_E_phase =   [ Data3[i][2] for i in range(Max1) ]
Inline_E_amp = [ Data1[i][3] for i in range(Max1) ]  
Inline_E_phase = [ Data1[i][4] for i in range(Max1) ]  
Vertical_E_amp = [ Data1[i][5] for i in range(Max1) ]  
Vertical_E_phase = [ Data1[i][6] for i in range(Max1) ]
      
Crossline_B_amp2 = [ Data12[i][1] for i in range(Max1) ]
Crossline_B_phase2 =   [ Data1[i][2] for i in range(Max1) ]
Inline_E_amp2 = [ Data12[i][3] for i in range(Max1) ]  
Inline_E_phase2 = [ Data12[i][4] for i in range(Max1) ]  
Vertical_E_amp2 = [ Data12[i][5] for i in range(Max1) ]  
Vertical_E_phase2 = [ Data12[i][6] for i in range(Max1) ]

fontTitle = {'family': 'serif', 'color':  'darkblue','weight': 'bold','size': 16 }
font = {'family': 'monospace', 'color':  'darkblue','weight': 'light','size': 12 }


fig, (ax, ax1) = plt.subplots( nrows=1, ncols=2, sharex=True,figsize=(12, 6))

ax.set_xlim(0,15000)
ax.set_xlabel('Range (m)', fontdict=font)
ax.set_ylabel('Amplitude', fontdict=font)
ax.set_title('Inline E Amplitude', fontdict=fontTitle)
ax.set_yscale('log')
ax.plot(RangeCross, Inline_E_amp, 'darkblue', label='model1')
ax.plot(RangeCross, Inline_E_amp2, 'r*', label='model2')
ax.tick_params(labelcolor='tab:orange')
ax.legend()
ax.grid()

ax1.set_xlim(0,15000)
ax1.set_xlabel('Range (m)', fontdict=font)
ax1.set_ylabel('Phase', fontdict=font)
ax1.set_title('Inline E Phase', fontdict=fontTitle)
ax1.plot(RangeCross,Inline_E_phase, 'darkblue', label='model1')
ax1.plot(RangeCross,Inline_E_phase2, 'r+', label='model2')
ax1.tick_params(labelcolor='tab:orange')
ax1.legend()
ax1.grid()

print(np.max(Inline_E_phase[3:]), np.argmax(Inline_E_phase[3:]), np.max(Crossline_E_phase[3:]), np.argmax(Crossline_E_phase[3:]))


print(RangeCross[12], RangeCross[17])
fig.set_facecolor('#eafff5')
plt. tight_layout()
plt.show()
fig.savefig('Question1_plot.png')


