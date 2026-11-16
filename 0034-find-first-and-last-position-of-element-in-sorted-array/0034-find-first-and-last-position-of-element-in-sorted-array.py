
class Solution(object):
    def searchRange(self, nums, target):
        first = -1
        last = -1

        # First binary search: Find first occurrence
        i = 0
        j = len(nums) - 1

        while i <= j:
            mid = i + (j - i) // 2

            if nums[mid] == target:
                first = mid
                j = mid - 1

            elif nums[mid] > target:
                j = mid - 1

            else:
                i = mid + 1

        if first == -1:
            return [-1, -1]

        # Second binary search: Find last occurrence
        left = first
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                last = mid
                left = mid + 1

            elif nums[mid] > target:
                right = mid - 1

            else:
                left = mid + 1

        return [first, last]
