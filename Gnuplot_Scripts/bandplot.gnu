EF= -2.4434
set xlabel "k-path"
set ylabel "Energy (eV)"
set grid
set yrange [-15:15]
set arrow from 0.577, graph 0 to 0.577, graph 1 nohead lc rgb "black" lt 2
set arrow from 0.910, graph 0 to 0.910, graph 1 nohead lc rgb "black" lt 2
set xtics ("{/Symbol G}" 0.0, "M" 0.577, "K" 0.910, "{/Symbol G}" 1.576)
plot "bands.dat.gnu" using 1:($2 - EF) with lines lw 2
