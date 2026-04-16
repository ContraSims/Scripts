#/bin/bash
path=$(pwd)
OUT="$path/band_gap.txt"
dir="0.95 0.96 0.97 0.98 0.99 1.00 1.01 1.02 1.03 1.04 1.05"

rm $OUT
for i in $dir; do
  cd $i
  cd bands
  if [ -f "BAND_GAP" ]; then
    chr=$(grep "Band Character:" BAND_GAP)    
    gap=$(grep "Band Gap (eV):" BAND_GAP)
    echo "$i : $gap , $chr">> $OUT
  else
    echo "$i : BAND_GAP not found" >>$OUT
  fi
     cd $path
done


