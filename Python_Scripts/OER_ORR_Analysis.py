import matplotlib.pyplot as plt
import numpy as np

def adsorption_energy(E_surface_adsorbate, E_surface, E_adsorbate):
    return E_surface_adsorbate - (E_surface + E_adsorbate)

def gibbs_free_energy(E_ads, ZPE, TS):
    return E_ads + ZPE - TS             

def oer_overpotential(delta_G_OH, delta_G_O, delta_G_OOH):
    delta_G_H2O = 0
    delta_G_O2 = 4.92
    U_theoretical = 1.23  
    delta_G1 = delta_G_OH - delta_G_H2O
    delta_G2 = delta_G_O - delta_G_OH
    delta_G3 = delta_G_OOH - delta_G_O
    delta_G4 = delta_G_O2 - delta_G_OOH
    delta_Gs = [delta_G1, delta_G2, delta_G3, delta_G4]
    max_G_step = max(delta_Gs)  
    oer_overpotential = max_G_step - U_theoretical  
    
    print("\n")
    print("#"*80)
    print("OXYGEN EVOLUTION REACTION (OER)")
    print("#"*80)
    print(f"G_H20: {delta_G_H2O:.8f} eV ~ {delta_G_H2O:.2f} eV")
    print(f"G1: {delta_G1:.8f} eV ~ {delta_G1:.2f} eV")
    print(f"G2: {delta_G2:.8f} eV ~ {delta_G2:.2f} eV")
    print(f"G3: {delta_G3:.8f} eV ~ {delta_G3:.2f} eV")
    print(f"G4: {delta_G4:.8f} eV ~ {delta_G4:.2f} eV")
    print(f"G_O2: {delta_G_O2:.8f} eV ~ {delta_G_O2:.2f} eV")
    print(f"Max G step: {max_G_step:.8f} eV ~ {max_G_step:.2f} eV")
    return oer_overpotential

def orr_overpotential(delta_G_OH, delta_G_O, delta_G_OOH):
    delta_G_H2O = 0
    delta_G_O2 = 4.92
    U_theoretical = 1.23  
    delta_G1 = delta_G_OOH - delta_G_O2
    delta_G2 = delta_G_O - delta_G_OOH
    delta_G3 = delta_G_OH - delta_G_O
    delta_G4 = delta_G_H2O - delta_G_OH
    delta_Gs = [delta_G1, delta_G2, delta_G3, delta_G4]
    max_G_step = max(delta_Gs) 
    orr_overpotential = max_G_step + U_theoretical  
    
    print("\n")
    print("#"*80)
    print("OXYGEN RUDUCTION REACTION (ORR)")
    print("#"*80)
    print(f"G_H20: {delta_G_H2O:.8f} eV ~ {delta_G_H2O:.2f} eV")
    print(f"G1: {delta_G1:.8f} eV ~ {delta_G1:.2f} eV")
    print(f"G2: {delta_G2:.8f} eV ~ {delta_G2:.2f} eV")
    print(f"G3: {delta_G3:.8f} eV ~ {delta_G3:.2f} eV")
    print(f"G4: {delta_G4:.8f} eV ~ {delta_G4:.2f} eV")
    print(f"G_O2: {delta_G_O2:.8f} eV ~ {delta_G_O2:.2f} eV")
    print(f"Min G step: {max_G_step:.8f} eV ~ {max_G_step:.2f} eV")
      
    return orr_overpotential
  

# Computed from DFT calculations
E_H2O = -14.21920481  # Reference energy for H2O
E_H2 = -6.77021166  # Reference energy for H2

# Zero point energy (ZPE) and entropy term (TS) corrections (in eV)
ZPE_H2O,TS_H2O = 0.57, 0.67
ZPE_H2,TS_H2 = 0.27, 0.40
ZPE_OH_ads, TS_OH_ads = 0.37, 0
ZPE_O_ads, TS_O_ads = 0.04, 0
ZPE_OOH_ads, TS_OOH_ads = 0.48, 0

# Liao, Peilin; Keith, John A.; Carter, Emily A. Water oxidation on pure and doped hematite (0001) surfaces: prediction of Co and Ni as effective dopants for electrocatalysis. Journal of the American Chemical Society, 2012, 134 (32), 13296–13309.

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# AT THIS POINT OF TIME VALUES NEED TO BE MANUALLY PLACED AT THE SPECIFIED FOR EACH INTERMEDIATE AT DIFFERENT ADSORPTION SITE AND CLEAN SURFACE

structure_name = r"$\mathbf{Ta_3SBr_7}$"            #Specify the structure name for which you want to perform OER and ORR analysis. This will be used in the plot titles and file names.

systems = {
    "S": {
        "OH": -275.16434537,                  #Energy of OH adsorbed on metal site
        "O": -271.31860860,                   #Energy of O adsorbed on metal site
        "OOH": -279.57288871                  #Energy of OOH adsorbed on metal site
    },

}

E_surface = -266.54662402                     #Energy of clean surface without any adsorbate


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

print("\n")
print("%"*80)
print("%"*80)
print("CODE FOR OER AND ORR ANALYSIS DEVELOPED BY ABHAY RAWAT")
print("GITHUB: https://github.com/ContraSims")
print("MAIL TO: arawat1909@gmail.com")
print("%"*80)
print("%"*80)



for site, energies in systems.items(): 
    print("\n")
    print("="*80)
    print(f"                            ADSORPTION SITE: {site} ")
    print("="*80)
    
    # Compute adsorption energies 
    delta_E_OH_ads = adsorption_energy(energies["OH"], E_surface, E_H2O - 0.5 * E_H2)
    delta_E_O_ads = adsorption_energy(energies["O"], E_surface, E_H2O - E_H2)
    delta_E_OOH_ads = adsorption_energy(energies["OOH"], E_surface, 2 * E_H2O - 1.5 * E_H2)
    
    print("\n")
    print("-"*80)
    print(f"ABSORPTION ENERGIES")
    print("-"*80)
    print(f"E_OH_on_{site}: {delta_E_OH_ads:.8f} eV")
    print(f"E_O_on_{site}: {delta_E_O_ads:.8f} eV")
    print(f"E_OOH_on_{site}: {delta_E_OOH_ads:.8f} eV")
    
    # Compute Gibbs free energies 
    delta_G_OH = gibbs_free_energy(delta_E_OH_ads, ZPE_OH_ads - (ZPE_H2O - 0.5 * ZPE_H2), TS_OH_ads - (TS_H2O - 0.5 * TS_H2))
    delta_G_O = gibbs_free_energy(delta_E_O_ads, ZPE_O_ads - (ZPE_H2O - ZPE_H2), TS_O_ads - (TS_H2O - TS_H2))
    delta_G_OOH = gibbs_free_energy(delta_E_OOH_ads, ZPE_OOH_ads - (2 * ZPE_H2O - 1.5 * ZPE_H2), TS_OOH_ads - (2 * TS_H2O - 1.5 * TS_H2))
    
    print("-"*80)
    print(f"GIBBS FREE ENERGIES OF INTERMEDIATES ON SUBSTRATE SITE")
    print("-"*80)
    print(f"G_OH_on_{site}: {delta_G_OH:.8f} eV ~ {delta_G_OH:.2f} eV")
    print(f"G_O_on_{site}: {delta_G_O:.8f} eV ~ {delta_G_O:.2f} eV")
    print(f"G_OOH_on_{site}: {delta_G_OOH:.8f} eV ~ {delta_G_OOH:.2f} eV")
    
    # Compute OER overpotential
    overpotential_OER = oer_overpotential(delta_G_OH, delta_G_O, delta_G_OOH)
    print("-"*80)
    print(f"OER OVERPOTENTIAL: {overpotential_OER:.8f} V ~ {overpotential_OER:.2f} V") 
    print("-"*80)
    
    steps = ['2H₂O(l)+*', '*OH', '*O', '*OOH', 'O₂(g)']
    delta_G = [0, delta_G_OH, delta_G_O, delta_G_OOH, 4.92]
    eta = overpotential_OER

    fig, ax = plt.subplots(figsize=(8, 6))
    delta = []
    for i in range(len(delta_G) - 1):
        ax.plot([i, i + 1], [delta_G[i]] * 2, color='black', lw=2)
        ax.plot([i + 1, i + 1], [delta_G[i], delta_G[i + 1]], color='black', lw=2, linestyle='--')
        delta.append(delta_G[i+1] - delta_G[i])
    ax.plot([len(delta_G) - 1, len(delta_G)], [delta_G[-1]] * 2, color='black', lw=2)
  
    max_delta = max(delta)

    for i in range(1, len(delta_G)):
        x = i + 0.04
        current_delta = delta[i-1]
        color = 'red' if np.isclose(current_delta, max_delta) else 'blue'

        if current_delta < 0 or current_delta > 0:
            y = (delta_G[i-1] + delta_G[i]) / 2 

        if current_delta > -0.1 and current_delta < 0.1:
            y = (delta_G[i-1] + delta_G[i]) / 2 - 0.2
            
        ax.text(x, y, f"{current_delta:.2f}", color=color, va='center', fontsize=12, fontweight='bold')

    ax.text(3.8, 0.6, f"η = {eta:.2f} V", color='red', fontsize=16, fontweight='bold')

    for i, (label, y_val) in enumerate(zip(steps, delta_G)):
        ax.text(i + 0.5, y_val + 0.1, label, ha='center', fontsize=12, fontweight='bold')

    ax.text(0.4, 4.0, f"{structure_name} --- {site}", fontsize=12, fontweight='bold')

    ax.set_xlim(0, len(steps))
    ax.set_ylim(-0.5, max(delta_G) + 1.0)
    ax.set_ylabel("ΔG (eV)", fontsize=18, fontweight='bold')
    ax.set_xlabel("Reaction Coordinates", fontsize=18, fontweight='bold')
    ax.set_xticks([])
    

    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(3)

    plt.tight_layout()
    plt.savefig(f"OER_{site}.png", dpi=600, bbox_inches='tight')
    print(f"OER Free Energy Diagram on {site} site plotted !!!")
    
    # Compute ORR overpotential
    overpotential_ORR = orr_overpotential(delta_G_OH, delta_G_O, delta_G_OOH)
    print("-"*80)
    print(f"ORR OVERPOTENTIAL: {overpotential_ORR:.8f} V ~ {overpotential_ORR:.2f} V")
    print("-"*80)
    print("\n")
    print(f"{site} site DONE !!!")
    
    steps.reverse()
    delta_G.reverse()
    eta = overpotential_ORR
 
    fig, ax = plt.subplots(figsize=(8, 6))  
    delta = []

    for i in range(len(delta_G) - 1):
        ax.plot([i, i + 1], [delta_G[i]] * 2, color='black', lw=2)  
        ax.plot([i + 1, i + 1], [delta_G[i], delta_G[i + 1]], color='black', lw=2, linestyle='--')  
        delta.append(delta_G[i+1] - delta_G[i])
    ax.plot([len(delta_G) - 1, len(delta_G)], [delta_G[-1]] * 2, color='black', lw=2)

    max_delta = max(delta)
    for i in range(1, len(delta_G)):
        x = i + 0.04 
        current_delta = delta[i-1]
        color = 'red' if np.isclose(current_delta, max_delta) else 'blue'

        if current_delta < 0 or current_delta > 0:
            y = (delta_G[i-1] + delta_G[i]) / 2 

        if current_delta > -0.1 and current_delta < 0:
            y = (delta_G[i-1] + delta_G[i]) / 2 - 0.2
            
        ax.text(x, y, f"{current_delta:.2f}", color=color, va='center', fontsize=12, fontweight='bold')

    ax.text(0.4, 0.6, f"η = {eta:.2f} V", color='red', fontsize=16, fontweight='bold')

    for i, (label, y_val) in enumerate(zip(steps, delta_G)):
        ax.text(i + 0.5, y_val + 0.1, label, ha='center', fontsize=12, fontweight='bold')

    ax.text(3.8, 4, f"{structure_name} --- {site}", fontsize=12, fontweight='bold')

    ax.set_xlim(0, len(steps))
    ax.set_ylim(-0.5, max(delta_G) + 1.0)
    ax.set_ylabel("ΔG (eV)", fontsize=18, fontweight='bold')
    ax.set_xlabel("Reaction Coordinates", fontsize=18, fontweight='bold')
    ax.set_xticks([])

    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(3)
    
    plt.tight_layout()
    plt.savefig(f"ORR_{site}.png", dpi=600, bbox_inches='tight')
    print(f"ORR Free Energy Diagram on {site} site plotted !!!")

    
print("\n")    
print("CALCULATIONS AND PLOTS FOR ALL SITES ARE COMPLETED !!!")
print("SEE YOU NEXT TIME [*_*] !!!")
print("\n")

