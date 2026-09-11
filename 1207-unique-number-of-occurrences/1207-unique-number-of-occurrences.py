class Solution(object):
    def uniqueOccurrences(self, arr):
        a=Counter(arr)
        b=set()
        for key,value in a.items():
            if value in b:
                return False
            else:
                b.add(value)
        return True