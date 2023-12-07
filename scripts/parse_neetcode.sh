while IFS= read -r line; do
    name=$(echo $line | awk '{$1=""; print $0}' | xargs)
    lock=$(leetcode list | grep "$name" | grep 🔒)
    echo "lock"
    echo $lock
    if [ ! -z "$lock" -a "$lock" != " " ]; then
        g=$(leetcode show "$name" -g -l python3 -x -o ./neetcode_problems_todo/ | grep "* Source Code:" | awk '{print $4}')
    fi
done < neetcode.txt