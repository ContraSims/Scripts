import numpy as np
import pandas as pd
from ase.io import read

path = "/home/pradhi/projects/collab/3d_AlOF/heterostructure/diff_F/1F/bader_charge/"

def read_potcar_zvals(potcar_path):
    """
    Reads POTCAR file and extracts ZVAL values.
    Handles lines with multiple key-value pairs separated by ';',
    such as 'POMASS = 207.200; ZVAL = 14.000 mass and valenz'.
    Returns list of ZVAL floats in the order they appear in POTCAR.
    """
    zvals = []
    with open(potcar_path, 'r') as f:
        for line in f:
            if 'ZVAL' in line:
                parts = line.split(';')
                for part in parts:
                    if 'ZVAL' in part:
                        try:
                            zval_str = part.split('=')[1].strip().split()[0]
                            zval = float(zval_str)
                            zvals.append(zval)
                        except Exception:
                            print(f"Warning: could not parse ZVAL from line: {line.strip()}")
                        break
    return zvals


def main():
    # Load the atomic structure (POSCAR or similar)
    atoms = read(path+'POSCAR')

    # Read ZVALs from POTCAR
    zval_list = read_potcar_zvals(path+'POTCAR')
   
    elements = []
    for atom in atoms:
        elements.append(atom.symbol)

    # Build a mapping element -> ZVAL (assumes POTCAR order matches unique elements order)
    unique_elements = []
    zval_dict = {}
    idx = 0
    for e in elements:
        if e not in unique_elements:
            unique_elements.append(e)
            zval_dict[e] = zval_list[idx]
            idx += 1
    
    df = pd.read_csv(path+'ACF.dat', delim_whitespace=True, skiprows=2, header=None)
    
    # Drop last 4 footer lines (non-numeric info)
    df = df[:-4]
    
    # Now df contains only atomic data rows; extract charge column (4th column, index 3)
    charges = df.iloc[:, 4].values  # since columns: X(0), Y(1), Z(2), CHARGE(3), ...
    
    print(charges)
    
    # Calculate net charge = charge - ZVAL for each atom
    net_charges = []
    for atom, charge in zip(atoms, charges):
        zval = zval_dict.get(atom.symbol)
        if zval is None:
           raise ValueError(f"ZVAL not found for element {atom.symbol}")
        net_charge = charge - zval
        net_charges.append(net_charge)
    
    net_charges = np.array(net_charges)
    # Create an array with indices as the first column
    indices = np.arange(len(net_charges))  # Create an array of indices
    net_charges_with_index = np.column_stack((indices, net_charges))  # Combine indices with net charges

    # Save net charges with index to file
    np.savetxt(path+'NetCharge.dat', net_charges_with_index, header='Index   NetCharge=(Charge - ZVAL)', fmt='%d      %.6f')    
    
    print("Net charges saved to NetCharge.dat")
   
    netchg=np.loadtxt(path+"NetCharge.dat")
    print("Sum of Bader charges is",np.sum(netchg[:,1]))

if __name__ == '__main__':
    main()    
