import numpy as np
import matplotlib.pyplot as plt

fe = np.loadtxt('formation.txt') 
x = fe[:,0]
fe_bisb = fe[:,1]
fe_bias = fe[:,2]

plt.figure(figsize=(8,6))
plt.plot(x, fe_bisb, marker='s', markersize=6, color='r',
         linewidth=2.5, markeredgecolor='black', label='BiSb')
plt.plot(x, fe_bias, marker='o', markersize=6, color='b',
         linewidth=2.5, markeredgecolor='black', label='BiAs')

plt.xlabel('Strain (%)', fontsize=16, fontweight='bold')
plt.ylabel('Formation Energy (eV)', fontsize=16, fontweight='bold')

plt.legend(fontsize=12)
plt.grid(True, linestyle='--', linewidth=0.6, alpha=0.8)

plt.tight_layout()
plt.savefig('formation_energy_vs_strain.png', dpi=600, bbox_inches='tight')

plt.show()
