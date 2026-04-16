#/bin/bash
path=$(pwd)
OUT="$path/fermi.txt"
dir="0.95 0.96 0.97 0.98 0.99 1.00 1.01 1.02 1.03 1.04 1.05"

rm $OUT
for i in $dir; do
  cd $i
  cd bands
  if [ -f "OUTCAR" ]; then
    fer=$(grep "E-fermi" OUTCAR)    
    echo "$i : $fer">> $OUT
  else
    echo "$i : OUTCAR not found" >>$OUT
  fi
     cd $path
done


