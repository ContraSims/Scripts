for d in 00 01 02 03 04 05 06; do
  E=$(grep "energy  without entropy" $d/OUTCAR | tail -1 | awk '{print $7}')
  echo "$d $E"
done > neb.dat
