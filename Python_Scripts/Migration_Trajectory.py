from ase.io import read, write

atoms_list = []

for i in range(10):  
    folder = f"{i:02d}"   
    f = f"{folder}/POSCAR"
    
    atoms = read(f)
    atoms_list.append(atoms)

write("neb.traj", atoms_list)


