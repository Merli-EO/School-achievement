fig2, (axe, axe1, axe2 ) = plt.subplots( nrows=1, ncols=3, sharex=True,figsize=(12, 6))


axe.set_xlim(0,15000)
axe.set_xlabel('Range (m)')
axe.set_ylabel('Amplitude')
axe.set_title('Amplitude( log&0 V/Am², T/Am)')
axe.set_yscale('log')
axe.plot(RangeCross, Crossline_B_amp)
axe.plot(RangeCross,Inline_E_amp)
axe.plot(RangeCross,Vertical_E_amp)
axe.plot(RangeCross, Crossline_B_phase)
axe.plot(RangeCross,Inline_E_phase)
axe.plot(RangeCross,Vertical_E_phase)
axe.grid()


axe1.set_xlim(0,15000)
axe1.set_xlabel('Range (m)')
axe1.set_ylabel('Amplitude')
axe1.set_title('Amplitude( log&0 V/Am², T/Am)')
axe1.set_yscale('log')
axe1.plot(RangeCross, Crossline_B_amp)
axe1.plot(RangeCross,Inline_E_amp)
axe1.plot(RangeCross,Vertical_E_amp)
axe1.plot(RangeCross, Crossline_B_phase)
axe1.plot(RangeCross,Inline_E_phase)
axe1.plot(RangeCross,Vertical_E_phase)
axe1.grid()


axe2.set_xlim(0,15000)
axe2.set_xlabel('Range (m)')
axe2.set_ylabel('Amplitude')
axe2.set_title('Amplitude( log&0 V/Am², T/Am)')
axe2.set_yscale('log')
axe2.plot(RangeCross, Crossline_B_amp)
axe2.plot(RangeCross,Inline_E_amp)
axe2.plot(RangeCross,Vertical_E_amp)
axe2.plot(RangeCross, Crossline_B_phase)
axe2.plot(RangeCross,Inline_E_phase)
axe2.grid()

Data2 = np.loadtxt("3ièmeSet.txt")
Data22 = np.loadtxt("3ièmeSet.txt")

Max2 = len(Data2)
RangeCross = [ Data2[i][0] for i in range(Max2) ]      #Range Cross
Crossline_Bis_amp = [ Data2[i][1] for i in range(Max2) ]
Cossliine_Bis_phase =   [ Data2[i][2] for i in range(Max2) ]
Inline_Eis_amp = [ Data2[i][3] for i in range(Max2) ]  
Inline_Eis_phase = [ Data2[i][4] for i in range(Max2) ]  
Vertical_Eis_amp = [ Data2[i][5] for i in range(Max2) ]  
Vertical_Eis_phase = [ Data2[i][6] for i in range(Max2) ]

Crossline_Bis_amp2 = [ Data22[i][1] for i in range(Max2) ]
Cossliine_Bis_phase2 =   [ Data22[i][2] for i in range(Max2) ]
Inline_Eis_amp2 = [ Data22[i][3] for i in range(Max2) ]  
Inline_Eis_phase2 = [ Data22[i][4] for i in range(Max2) ]  
Vertical_Eis_amp2 = [ Data22[i][5] for i in range(Max2) ]  
Vertical_Eis_phase2 = [ Data22[i][6] for i in range(Max2) ]


ax2.set_xlim(0,15000)
ax2.set_xlabel('Range (m)')
ax2.set_ylabel('Amplitude')
ax2.set_title('Amplitude( log&0 V/Am², T/Am)')
ax2.set_yscale('log')
#ax2.plot(RangeCross, Crossline_B_amp)
ax2.plot(RangeCross,Inline_E_amp)
ax2.plot(RangeCross,Vertical_E_amp)
ax2.plot(RangeCross, Crossline_B_phase)
ax2.plot(RangeCross,Inline_E_phase)
ax2.plot(RangeCross,Vertical_E_phase)
ax2.grid()




