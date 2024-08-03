class Solution(object):
    def romanToInt(self, s):
        x={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        y=0
        s=s.replace("IV","IIII").replace("IX","VIIII").replace("XL","XXXX").replace("XC","LXXXX").replace("CD","CCCC").replace("CM","DCCCC")
        for i in s:
            y+=x[i]
        return y
