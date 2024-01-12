import matplotlib.pyplot  as plt
import numpy as np


Data0 = np.loadtxt("Premier_Graphe_bis.txt")
Data02 = np.loadtxt("1erSet2.txt")

Max0 = len(Data0)
RangeCross = [ Data0[i][0] for i in range(Max0) ]      #Range Cross
Crossline_E_amp = [ Data0[i][1] for i in range(Max0) ]
Crossline_E_phase =   [ Data0[i][2] for i in range(Max0) ]
Inline_B_amp = [ Data0[i][3] for i in range(Max0) ]  
Inline_B_phase = [ Data0[i][4] for i in range(Max0) ]  
Vertical_B_amp = [ Data0[i][5] for i in range(Max0) ]  
Vertical_B_phase = [ Data0[i][6] for i in range(Max0) ]

Crossline_E_amp2 = [ Data02[i][1] for i in range(Max0) ]
Crossline_E_phase2 =   [ Data02[i][2] for i in range(Max0) ]
Inline_B_amp2 = [ Data02[i][3] for i in range(Max0) ]  
Inline_B_phase2 = [ Data02[i][4] for i in range(Max0) ]  
Vertical_B_amp2 = [ Data02[i][5] for i in range(Max0) ]  
Vertical_B_phase2 = [ Data02[i][6] for i in range(Max0) ]

fig, (ax, ax1) = plt.subplots( nrows=1, ncols=2, sharex=True,figsize=(12, 6))

ax.set_xlim(0,15000)
ax.set_xlabel('Range (m)')
ax.set_ylabel('Amplitude')
ax.set_title('Amplitude( log&0 V/Am², T/Am)')
ax.set_yscale('log')
ax.plot(RangeCross, Crossline_E_amp)
#ax.plot(RangeCross,Inline_B_amp)
ax.plot(RangeCross, Crossline_E_amp2, 'r--')
#ax.plot(RangeCross,Inline_B_amp2)



ax.grid()

Data1 = np.loadtxt("2ièmeSet.txt")
Data12 = np.loadtxt("2ièmeSet.txt")

Max1 = len(Data1)
RangeCross = [ Data1[i][0] for i in range(Max1) ]      #Range Cross
Crossline_B_amp = [ Data1[i][1] for i in range(Max1) ]
Crossline_B_phase =   [ Data1[i][2] for i in range(Max1) ]
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



ax1.set_xlim(0,15000)
ax1.set_xlabel('Range (m)')
ax1.set_ylabel('Phase')
ax1.set_title('Phase')
#ax1.set_yscale('log')
#ax1.plot(RangeCross, Crossline_B_phase)
ax1.plot(RangeCross,Inline_E_phase, 'darkblue')
#ax1.plot(RangeCross, Crossline_B_phase2)
ax1.plot(RangeCross,Inline_E_phase2, 'r+')
ax1.grid()



plt. tight_layout()
plt.show()


