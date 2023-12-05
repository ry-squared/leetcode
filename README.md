# Progress

## Easy

![14](https://progress-bar.dev/14/?scale=28&suffix=/28)

## Medium

![4](https://progress-bar.dev/4/?scale=101&suffix=/101)

## Hard

![1](https://progress-bar.dev/1/?scale=21&suffix=/21)

# Description

### 150 curated Neetcode problems from easy to hard:

-   [neetcode problems by category](https://neetcode.io/practice)
-   [neetcode list in full](https://leetcode.com/list/rr2ss0g5/)
-   [neetcode list as .txt](neetcode.txt)

# Getting Started:

Intalll (unofficial) leetcode CLI

    # v8 node seems to be supported
    brew install nvm
    brew install libsecret   
    nvm install 8
    nvm use 8
    npm install -g leetcode-cli
    leetcode version

Download plugins

    # login to chrome desktop -> then install and enable
    leetcode plugin -i cookie.chrome
    leetcode plugin -e cookie.chrome

## Project Commands:

calculate completions stats

    ./scripts/stats.sh

## Leetcode Commands:

Show problem:

    leetcode show 217

Download problem:

    # download problem 217, generate source file + add question, as python3 script
    # header of file added using "-x" flag is needed to distinguish python3 vs python2 for submission
    leetcode show 217 -g -x -l python3 

Submit to leetcode test cases:

    # submit
    leetcode submit ./1.two-sum.py
