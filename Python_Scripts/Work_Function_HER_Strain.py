import matplotlib.pyplot as plt
import numpy as np

dat = np.loadtxt('Wf_GibbsE_Strain.txt')

st = dat[:,0]
wf = dat[:,1]
ge = dat[:,2]

fig, ax1 = plt.subplots(figsize=(8, 6))

ax1.set_xlabel('Strain (%)', fontsize=18, fontweight='bold')
ax1.set_ylabel(r'Work Function $\mathbf{\Phi\, (eV \AA)}$', color='r', fontsize=18, fontweight='bold')

ax1.plot(st, wf, marker='s', markersize=10,linestyle='-', linewidth = 4, color='r', markeredgecolor='black', label=r'$\mathbf{\Phi}$')
ax1.tick_params(axis='y', labelcolor='r')

ax2 = ax1.twinx()

ax2.set_ylabel(r'Gibbs Free Energy $\mathbf{\Delta G_{H^*}}$ (eV)', color='b', fontsize=18, fontweight='bold')

ax2.plot(st, ge, marker='o', markersize=10, linestyle='-', linewidth = 4, color='b', markeredgecolor='black', label=r'$\mathbf{\Delta G_H^*}$')
ax2.tick_params(axis='y', labelcolor='b')

ax1.grid(axis='x', linestyle='--', linewidth=0.6, alpha=0.8)  
ax1.grid(axis='y', linestyle='--', linewidth=0.6, alpha=0.8)  

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper center', bbox_to_anchor=(0.5, 1), ncol=2)

fig.tight_layout()
plt.savefig('Work_Function_HER_vs_strain.png', dpi=600, bbox_inches='tight')
plt.show()
