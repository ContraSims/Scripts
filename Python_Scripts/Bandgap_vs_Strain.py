import numpy as np
import matplotlib.pyplot as plt

bg = np.loadtxt('band.txt') 
x = bg[:,0]
bg_bisb = bg[:,1]
bg_bias = bg[:,2]

plt.figure(figsize=(8,6))
plt.plot(x, bg_bisb, marker='s', markersize=10, color='r',
         linewidth=4, markeredgecolor='black', label='BiSb')
plt.plot(x, bg_bias, marker='o', markersize=10, color='b',
         linewidth=4, markeredgecolor='black', label='BiAs')

plt.xlabel('Strain (%)', fontsize=18, fontweight='bold')
plt.ylabel(r'Band Gap $\mathbf{E_g}$ (eV)', fontsize=18, fontweight='bold')

plt.legend(fontsize=12)
plt.grid(True, linestyle='--', linewidth=0.6, alpha=0.8)

plt.tight_layout()
plt.savefig('bandgap_vs_strain.png', dpi=600, bbox_inches='tight')

plt.show()
