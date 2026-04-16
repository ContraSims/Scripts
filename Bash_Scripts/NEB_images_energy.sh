for d in 00 01 02 03 04 05 06; do
  E=$(grep "free  energy   TOTEN" $d/OUTCAR | tail -1 | awk '{print $5}')
  echo "$d $E"
done > neb.dat

