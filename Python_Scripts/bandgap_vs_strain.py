import numpy as np
import matplotlib.pyplot as plt

bg = np.loadtxt('band.txt') 
x = bg[:,0]
bg_bisb = bg[:,1]
bg_bias = bg[:,2]

plt.figure(figsize=(8,5))
plt.plot(x, bg_bisb, marker='s', markersize=6, color='r',
         linewidth=2.5, markeredgecolor='black', label='BiSb')
plt.plot(x, bg_bias, marker='o', markersize=6, color='b',
         linewidth=2.5, markeredgecolor='black', label='BiAs')

plt.xlabel('Strain (%)', fontsize=16, fontweight='bold')
plt.ylabel(r'Band Gap $\mathbf{E_g}$ (eV)', fontsize=16, fontweight='bold')

plt.legend(fontsize=12)
plt.grid(True, linestyle='--', linewidth=0.6, alpha=0.8)

plt.tight_layout()
plt.savefig('bandgap_vs_strain.png', dpi=600, bbox_inches='tight')

plt.show()
