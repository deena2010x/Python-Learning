class Solution(object):
    def lengthOfLastWord(self, s):
        words=s.rstrip().split(" ")
        lastWord=words[-1]
        length=len(lastWord)
        return length    
