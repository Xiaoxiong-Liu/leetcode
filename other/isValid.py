“”“
 有效的括号

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/26/others/68/

”“”

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s=='':
            return True
        stack = []
        for i in range(len(s)):
            if s[i] in ('(','[','{'):
                stack.append(s[i])
            elif s[i] in (')',']','}'):
                if len(stack)==0:
                    return False
                t = stack.pop()
                if s[i] == ')' and t!='(' or  s[i] ==']' and t!='[' or  s[i]=='}' and t!='{':
                    return False
        if len(stack)==0:
            return True
        else:
            return False
