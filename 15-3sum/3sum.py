class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        list = []
        nums.sort()
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l<r:
                countSum = n + nums[l] +nums[r]
                if countSum < 0:
                    l += 1
                elif countSum > 0:
                    r -= 1
                else:
                    list.append([n,nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

        return list