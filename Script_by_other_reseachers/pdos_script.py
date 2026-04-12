import sys

def process_file(input_file, output_file):
    with open(input_file, 'r') as fin, open(output_file, 'w') as fout:
        next(fin, None)
        fout.write(f"{'#E(eV)':<10}{'s':<8}{'p':<8}{'d':<8}{'total_dos':<8}\n")
        for line in fin:
            if not line.strip():
                continue

            parts = line.split()

            if len(parts) < 5:
                print("Warning: Skipping line with insufficient columns:", line.strip())
                continue

            try:
                col1 = parts[0]
                col2 = parts[1]

                sum_3to5 = float(parts[2]) + float(parts[3]) + float(parts[4])
                sum_6to10 = float(parts[5]) + float(parts[6]) + float(parts[7]) + float(parts[8]) + float(parts[9])
                sum_tot = float(parts[10])

                fout.write(f"{col1} {col2} {sum_3to5:.5f} {sum_6to10:.5f} {sum_tot}\n")
            except ValueError:
                print("Error converting line to float, skipping:", line.strip())
                continue

if __name__ == "__main__":
    input_filename = 'PDOS_Bi_SOC.dat'
    output_filename = 'PDOS_Bi_SOC_sum.dat'
    process_file(input_filename, output_filename)
