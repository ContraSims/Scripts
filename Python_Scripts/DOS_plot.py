import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("dos.dat")
Ef = -2.438
E = data[:,0] - Ef
DOS = data[:,1]

plt.plot(E, DOS)
plt.axvline(0, linestyle='--')
plt.xlim(-5,5)
plt.ylim(0,1.4)
plt.xlabel("Energy (eV)")
plt.ylabel("DOS")
plt.show()
