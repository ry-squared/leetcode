g=$(leetcode show  $1 -g -l python3 -x | grep "* Source Code:" | awk '{print $4}') 
mv $g ${g}3