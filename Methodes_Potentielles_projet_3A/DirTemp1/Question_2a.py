Crossline_E_amp0025 = [ Data10025[i][1] for i in range(Max1) ]  
Crossline_E_phase0025 = [ Data10025[i][2] for i in range(Max1) ]  
Crossline_E_amp20025 = [ Data20025[i][1] for i in range(Max1) ]  
Crossline_E_phase20025 = [ Data20025[i][2] for i in range(Max1) ]  
Crossline_E_amp05 = [ Data105[i][1] for i in range(Max1) ]  
Crossline_E_phase05 = [ Data105[i][2] for i in range(Max1) ]  
Crossline_E_amp205 = [ Data205[i][1] for i in range(Max1) ]  
Crossline_E_phase205 = [ Data205[i][2] for i in range(Max1) ] 
Crossline_E_amp1 = [ Data11[i][1] for i in range(Max1) ]  
Crossline_E_phase1 = [ Data11[i][2] for i in range(Max1) ]  
Crossline_E_amp21 = [ Data21[i][1] for i in range(Max1) ]  
Crossline_E_phase21 = [ Data21[i][2] for i in range(Max1) ] 
Crossline_E_amp25 = [ Data125[i][1] for i in range(Max1) ]  
Crossline_E_phase25 = [ Data125[i][2] for i in range(Max1) ]  
Crossline_E_amp225 = [ Data225[i][1] for i in range(Max1) ]  
Crossline_E_phase225 = [ Data225[i][2] for i in range(Max1) ] 
ax.plot(RangeCross, Crossline_E_amp0025, 'darkgreen', label='model1 f=0.025Hz')
ax.plot(RangeCross, Crossline_E_amp20025, 'b3', label='model2 f=0.025Hz')
ax.plot(RangeCross, Crossline_E_amp05, 'lightblue', label='model1 f =0.5Hz')
ax.plot(RangeCross, Crossline_E_amp205, 'g2', label='model2 f=0.5Hz')
ax.plot(RangeCross, Crossline_E_amp1, 'lightgreen', label='model1 f=1Hz')
ax.plot(RangeCross, Crossline_E_amp21, 'k1', label='model2 f=1Hz')
ax.plot(RangeCross, Crossline_E_amp25, 'darkblue', label='model1 f=0.25Hz')
ax.plot(RangeCross, Crossline_E_amp225, 'r*', label='model2 f=0.25')
ax1.plot(RangeCross,Crossline_E_phase0025, 'darkgreen', label='model1 f=0.025Hz')
ax1.plot(RangeCross,Crossline_E_phase20025, 'b3', label='model2 f=0.025Hz')
ax1.plot(RangeCross,Crossline_E_phase05, 'lightblue', label='model1 f=0.5')
ax1.plot(RangeCross,Crossline_E_phase205, 'g2', label='model2 f=0.5Hz')
ax1.plot(RangeCross,Crossline_E_phase1, 'lightgreen', label='model1 f=1Hz')
ax1.plot(RangeCross,Crossline_E_phase21, 'k1', label='model2 f=1Hz')
ax1.plot(RangeCross,Crossline_E_phase25, 'darkblue', label='model1 f=0.25Hz')
ax1.plot(RangeCross,Crossline_E_phase225, 'r+', label='model2 f=0.25Hz')
