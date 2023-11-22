# v8 of node seems to work
brew install nvm
brew install libsecret   
nvm install 8
nvm use 8

# login to chrom desktop -> then install and enable
leetcode plugin -i cookie.chrome
leetcode plugin -e cookie.chrome

#### example commands ####

# submit
leetcode submit ./1.two-sum.py3 

# show problem 217
leetcode show -c 217

# download problem 217 and change extension to py3
g=$(leetcode show  -g 217 -l python3 | grep "* Source Code:" | awk '{print $4}') 
mv $g ${g}3