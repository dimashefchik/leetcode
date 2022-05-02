# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        re = 0
        while len(s) > 0:
            if len(s) > 1 and 'CM' in s:
                s = s.replace('CM', '')
                re += 900
            elif len(s) > 1 and 'CD' in s:
                s = s.replace('CD', '')
                re += 400
            elif len(s) > 1 and 'XC' in s:
                s = s.replace('XC', '')
                re += 90
            elif len(s) > 1 and 'XL' in s:
                s = s.replace('XL', '')
                re += 40
            elif len(s) > 1 and 'IX' in s:
                s = s.replace('IX', '')
                re += 9
            elif len(s) > 1 and 'IV' in s:
                s = s.replace('IV', '')
                re += 4
            else:
                if 'M' in s:
                    s = s.replace('M', '',1)
                    re += 1000
                elif 'D' in s:
                    s = s.replace('D', '',1)
                    re += 500
                elif 'C' in s:
                    s = s.replace('C', '',1)
                    re += 100
                elif 'L' in s:
                    s = s.replace('L', '',1)
                    re += 50
                elif 'X' in s:
                    s = s.replace('X', '',1)
                    re += 10
                elif 'V' in s:
                    s = s.replace('V', '',1)
                    re += 5
                elif 'I' in s:
                    s = s.replace('I', '',1)
                    re += 1
        return re
