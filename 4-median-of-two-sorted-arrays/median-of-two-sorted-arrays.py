class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = nums1 + nums2
        num.sort()
        total = len(num)
        if total % 2 == 1:
            return float(num[total // 2])
        else:
            middle1 = num[total // 2 - 1]
            middle2 = num[total // 2]
            return (float(middle1) + float(middle2)) / 2.0

        
    