class Solution(object):
    def permute(self, nums):
        def nik(n):
            if n == 0 or n == 1:
                return 1
            return n * nik(n - 1)

        a = nik(len(nums))
        nums.sort()
        b = []

        def nextperm(nums):
            n = len(nums)
            i = n - 2

            while i >= 0 and nums[i] >= nums[i + 1]:
                i -= 1

            if i >= 0:
                j = n - 1
                while nums[j] <= nums[i]:
                    j -= 1
                nums[i], nums[j] = nums[j], nums[i]

            nums[i + 1:] = reversed(nums[i + 1:])

        for _ in range(a):
            b.append(nums[:])
            nextperm(nums)

        return b