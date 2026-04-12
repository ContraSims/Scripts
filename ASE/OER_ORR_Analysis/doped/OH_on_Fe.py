from ase.io import read, write
from ase.build import molecule
import numpy as np

slab = read("CONTCAR")

index = 11                                                              # Substrate atom index in POSCAR/CONTCAR
pos = slab.positions[index]                                             # Coordinates of substrate atom (array)

OH = molecule('OH')                
OH.rotate(180, 'x', center=OH[0].position)                              # rotates molecule (angle, axis, center of rotation)
 
h = 2.00                                                                # Adsorption distance Fe--O

OH.translate(pos + np.array([0, 0, h]) - OH[0].position)                # moves molecule along a vector (target_position - current_position)
 
slab += OH                                                              # Merge molecule and slab

write("OH_on_Fe.vasp", slab, format="vasp", direct=True)

print("DONE!!!")
