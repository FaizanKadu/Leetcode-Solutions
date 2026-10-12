class Solution(object):
    def twoSum(self, nums, target):
        dictn = dict()
        x = 0
        for i in nums:
            dictn[i] = x
            x+=1
        for j in range(len(nums)):
            y = target - nums[j]
            if y in dictn and dictn[y]!=j:
                return [j, dictn[y]]
        