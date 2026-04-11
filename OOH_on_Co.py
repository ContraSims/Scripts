from ase.io import read, write
from ase.build import molecule
import numpy as np

slab = read("CONTCAR")

index = 10
pos = slab.positions[index]

OOH = molecule('H2O2')
del OOH[-1]                           # Removes last H atom

OOH.rotate(90, 'x', center=OOH[0].position)

h = 1.95

OOH.translate(pos + np.array([0, 0, h]) - OOH[1].position)

slab += OOH

write("OOH_on_Co.vasp", slab, format="vasp", direct=True)

print("DONE!!!")
