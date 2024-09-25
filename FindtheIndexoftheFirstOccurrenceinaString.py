class Solution(object):
    def strStr(self, haystack, needle):
        m=len(haystack)
        n=len(needle)
        x=0
        for i in range(0,m-n+1):
            if haystack[i:i+n]==needle:
                return i
        return -1
