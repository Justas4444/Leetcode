class Solution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def twoSum(self):
        numToIndex = {}
        for i in range(len(self.nums)):
            if self.target - self.nums[i] in numToIndex:
                return [numToIndex[self.target - self.nums[i]], i]
            numToIndex[self.nums[i]] = i
        return []

Nums1 = Solution([1,2,3,4,5,6,7,8,9,10,11,12,13,14], 7)


result = Nums1.twoSum()

print(result)