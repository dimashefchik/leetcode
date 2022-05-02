# https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)

        while True:
            a = s_list.count('#')

            if  a != 0:
                x = s_list.index('#')
                if x == 0:
                    s_list.remove('#')
                else:
                    s_list.remove('#')
                    s_list.pop(x - 1)
            else:
                break
        while True:
            b = t_list.count('#')

            if b != 0:
                x = t_list.index('#')
                if x == 0:
                    t_list.remove("#")
                else:
                    t_list.remove('#')
                    t_list.pop(x - 1)
            else:
                break

        return s_list == t_list
