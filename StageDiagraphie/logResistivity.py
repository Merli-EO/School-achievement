import numpy as np 
import matplotlib.pyplot as plt

fontTitle = {'family': 'serif', 'color':  'darkblue','weight': 'normal','size': 16,}
font = {'family': 'monospace', 'color':  'darkblue','weight': 'light','size': 12 }


resistivityLogDescente = np.loadtxt("/Users/merliemmanuelendamneobiang/Downloads/250521_F1b_descente1.txt")
resistivityLogMontee = np.loadtxt("/Users/merliemmanuelendamneobiang/Downloads/250521_F1b_monte1.txt")



depthD = [ cellule[0] for cellule in resistivityLogDescente]

RX8D = [ cellule[1] for cellule in resistivityLogDescente]

RX16D = [ cellule[2] for cellule in resistivityLogDescente]

RX32D = [ cellule[3] for cellule in resistivityLogDescente]

RX64D = [ cellule[4] for cellule in resistivityLogDescente]

depthM = [ cellule[0] for cellule in resistivityLogMontee]

RX8M = [ cellule[1] for cellule in resistivityLogMontee]

RX16M = [ cellule[2] for cellule in resistivityLogMontee]

RX32M = [ cellule[3] for cellule in resistivityLogMontee]

RX64M = [ cellule[4] for cellule in resistivityLogMontee]

ligne33M = [ 33.5 for i in range(len(resistivityLogMontee))]
ligne36M = [ 36 for i in range(len(resistivityLogMontee)) ]

ligne33D = [ 33.5 for i in range(len(resistivityLogDescente))]
ligne36D = [ 36 for i in range(len(resistivityLogDescente)) ]

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, sharey=True)

ax1.plot(np.log10(RX8D), depthD, label="RX8")
ax1.plot(np.log10(RX16D), depthD, label="RX16")
ax1.plot(np.log10(RX32D), depthD, label="RX32")
ax1.plot(np.log10(RX64D), depthD, label="RX64")
#ax1.plot(depthD, ligne33D, "k--")
#ax1.plot(depthD, ligne36D, "k--")
ax1.set_xlabel(r'résistivité [$\Omega$.m]', fontdict=font)
ax1.set_ylabel('profondeur en [m]', fontdict=font)
ax1.invert_yaxis()
ax1.set_title(" log de résistivité \n en descente", fontdict=fontTitle)
ax1.grid()
ax1.tick_params(labelcolor='tab:cyan')
ax1.set_facecolor('#eafff5')
ax1.legend()

ax2.plot(np.log10(RX8M), depthM, label="RX8")
ax2.plot(np.log10(RX16M), depthM, label="RX16")
ax2.plot(np.log10(RX32M), depthM, label="RX32")
ax2.plot(np.log10(RX64M), depthM, label="RX64")
#ax2.plot(depthM, ligne33M, "k--")
#ax2.plot(depthM, ligne36M, "k--")
ax2.set_xlabel(r'résistivité [$\Omega$.m]', fontdict=font)
#ax2.invert_yaxis()
ax2.set_title("log de résistivité \n en montée", fontdict=fontTitle)
ax2.grid()
ax2.tick_params(labelcolor='tab:cyan')
ax2.set_facecolor('#eafff5')
ax2.legend()

plt.tight_layout
plt.show()
fig.savefig("resistivityLogF1b.png", dpi='figure')