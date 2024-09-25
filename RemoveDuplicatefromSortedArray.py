class Solution(object):
    def removeDuplicates(self, nums):
        k=0
        for i in nums:
            if k<1 or i>nums[k-1]:
                nums[k]=i
                k+=1
        return k
