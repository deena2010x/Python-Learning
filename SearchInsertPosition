class Solution(object):
    def searchInsert(self, nums, target):
        length=len(nums)
        for i in range(0,length):
            if nums[i]==target:
                return i
        if target not in nums:
            for i in range(0,length):
                if target<nums[i]:
                    return i
        return length
