class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        a=Counter(magazine)
        for i in ransomNote:
            if i not in a:
                return False
            if a[i]==1:
                del a[i]
            else:
                a[i]-=1
        return True
        