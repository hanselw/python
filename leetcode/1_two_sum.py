class Sulotion:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, a in enumerate(nums):
            b = target - a
            if b in nums[i+1:]:
                i2 = nums[i+1:].index(b)+i+1
                return [i, i2]

