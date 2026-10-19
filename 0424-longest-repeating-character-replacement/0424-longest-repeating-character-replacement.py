class Solution(object):
    def characterReplacement(self, s, k):
        a = {}
        max_freq = 0
        max_length = 0
        left = 0

        for i in range(len(s)):
            a[s[i]] = a.get(s[i], 0) + 1
            max_freq = max(max_freq, a[s[i]])

            wind = i - left + 1

            while wind - max_freq > k:
                a[s[left]] -= 1
                left += 1
                wind = i - left + 1

            max_length = max(max_length, i - left + 1)

        return max_length