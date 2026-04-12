from ase.io import read, write
from ase.build import molecule
import numpy as np

slab = read("CONTCAR")

index = 1                                                              # Substrate atom index in POSCAR/CONTCAR
pos = slab.positions[index]                                            # Coordinates of substrate atom (array)

O = molecule('O')                                            

h = 2.00                                                               # Adsorption distance Cu--O

O.translate(pos + np.array([0, 0, h]) - O[0].position)                 # moves molecule along a vector (target_position - current_position)

slab += O                                                              # Merge molecule and slab

write("O_on_Cu.vasp", slab, format="vasp", direct=True)

print("DONE!!!")
