class Solution(object):
    def removeDuplicates(self, nums):
        x=0
        for i in nums:
            if x<1 or i>nums[x-1]:
                nums[x]=i
                x+=1
        return x
