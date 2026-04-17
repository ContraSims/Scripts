import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('neb.dat')
images = data[:, 0]
energies = data[:, 1]
energies -= energies[0]  

plt.plot(images, energies, 'o-', color='blue')

plt.xlabel('Images')
plt.ylabel('Relative Energy (eV)')
plt.title('NEB Migration Barrier')

plt.grid(True)
plt.tight_layout()
plt.savefig("neb_barrier.png", dpi=600)
plt.show()

