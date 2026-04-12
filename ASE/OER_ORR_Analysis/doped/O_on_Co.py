from ase.io import read, write
from ase.build import molecule
import numpy as np

slab = read("CONTCAR")

index = 10                                                             # Substrate atom index in POSCAR/CONTCAR
pos = slab.positions[index]                                            # Coordinates of substrate atom (array)

O = molecule('O')                                          

h = 1.95                                                               # Adsorption distance Co--O

O.translate(pos + np.array([0, 0, h]) - O[0].position)                 # moves molecule along a vector (target_position - current_position)

slab += O                                                              # Merge molecule and slab

write("O_on_Co.vasp", slab, format="vasp", direct=True)

print("DONE!!!")
