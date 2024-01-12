import matplotlib.pyplot  as plt
import numpy as np



Data1 = np.loadtxt("set2_model1")
Data12 = np.loadtxt("2ièmeSet2.txt")

Max1 = len(Data1)
RangeCross = [ Data1[i][0] for i in range(Max1) ]      #Range Cross
Crossline_E_amp = [ Data1[i][1] for i in range(Max1) ]
Crossline_E_phase =   [ Data1[i][2] for i in range(Max1) ]
Inline_E_amp = np.array([ Data1[i][3] for i in range(Max1) ] ) 
Inline_E_phase = [ Data1[i][4] for i in range(Max1) ]  
Vertical_E_amp = [ Data1[i][5] for i in range(Max1) ]  
Vertical_E_phase = [ Data1[i][6] for i in range(Max1) ]
      
Crossline_E_amp2 = [ Data12[i][1] for i in range(Max1) ]
Crossline_E_phase2 =   [ Data1[i][2] for i in range(Max1) ]
Inline_E_amp2 = np.array([ Data12[i][3] for i in range(Max1) ])  
Inline_E_phase2 = [ Data12[i][4] for i in range(Max1) ]  
Vertical_E_amp2 = [ Data12[i][5] for i in range(Max1) ]  
Vertical_E_phase2 = [ Data12[i][6] for i in range(Max1) ]

fontTitle = {'family': 'serif', 'color':  'darkblue','weight': 'bold','size': 16 }
font = {'family': 'monospace', 'color':  'darkblue','weight': 'light','size': 12 }

NAR = (Inline_E_amp2)/Inline_E_amp
print(np.max(NAR))
fig, ax = plt.subplots( nrows=1, ncols=1, sharex=False,figsize=(12, 6))

ax.set_xlim(0,15000)
ax.set_xlabel('Range (m)', fontdict=font)
ax.set_ylabel('Amplitude', fontdict=font)
ax.set_title('NAR ', fontdict=fontTitle)
#ax.set_yscale('log')
ax.plot(RangeCross, NAR, 'darkblue', label='NAR')
ax.text( 7000, 1.007, "NAR = 1.01091", size=14, rotation=-30, fontstyle="italic", backgroundcolor="cyan")
#ax.arrow( 6500, 1.007, (-6500+4200), -1.01091 + 1.007)
#ax.plot(RangeCross, Crossline_E_amp2, 'r*', label='model2')
ax.tick_params(labelcolor='tab:orange')
ax.legend()
ax.grid()

#ax1.set_xlim(0,15000)
#ax1.set_xlabel('Range (m)', fontdict=font)
#ax1.set_ylabel('Phase', fontdict=font)
#ax1.set_title('Crossline E Phase', fontdict=fontTitle)
#ax1.plot(RangeCross,Crossline_E_phase, 'darkblue', label='model1')
#ax1.plot(RangeCross,Crossline_E_phase2, 'r+', label='model2')
#ax1.tick_params(labelcolor='tab:orange')
#ax1.legend()
#ax1.grid()


fig.set_facecolor('#eafff5')
plt. tight_layout()
plt.show()
fig.savefig('Question2e_plot.png')

