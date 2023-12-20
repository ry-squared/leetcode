#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (73.67%)
# Total Accepted:    1.6M
# Total Submissions: 2.2M
# Testcase Example:  '3'
#
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
# Input: n = 1
# Output: ["()"]
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 8
# 
# 
#
class Solution:

    def __init__(self) -> None:
        self.parens_combos = []

    def dfs(self,paren,left_paren_count, right_paren_count,n, paren_str):
        

        # paren rules:
        # must start with "("
        # if open, must be closed
        # can't close if not open

        if paren == "(":
            if left_paren_count < n:
                left_paren_count+=1
                paren_str+="("
        elif paren == ")" and right_paren_count<left_paren_count:
            if right_paren_count < n:
                right_paren_count+=1
                paren_str+=")"
        else:
            return None

                
        if left_paren_count==n and right_paren_count==n:
            self.parens_combos.append(paren_str)
        elif left_paren_count<n and right_paren_count<n:
            self.dfs("(",left_paren_count, right_paren_count, n,paren_str)
            self.dfs(")",left_paren_count, right_paren_count, n,paren_str)
        elif left_paren_count==n and right_paren_count<n:
            self.dfs(")",left_paren_count, right_paren_count, n,paren_str)
        elif left_paren_count<n and right_paren_count==n:
            self.dfs("(",left_paren_count, right_paren_count, n,paren_str)
    

    def generateParenthesis(self, n: int) -> List[str]:
                
        self.dfs("(", 0,0, n, paren_str="")

        return self.parens_combos