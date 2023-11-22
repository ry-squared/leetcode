convert -size 450x100 xc:white -pointsize 12 -gravity center -fill black -draw "text 0,0 \"$(cat stats.txt)\""  stats.png
