while IFS= read -r line; do
    name=$(echo $line | awk '{$1=""; print $0}' | xargs)
    g=$(leetcode show "$name" -g -l python3 -x -o . | grep "* Source Code:" | awk '{print $4}')
done < neetcode.txt