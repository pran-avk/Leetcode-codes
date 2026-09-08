class Solution(object):
    def checkInclusion(self, s1, s2):
        a=Counter(s1)
        b=Counter(s2[0:len(s1)])
        if len(s1)>len(s2):
            return False
        if a==b:
            return True
        for i in range(1,len(s2)-len(s1)+1):
            if b[s2[i-1]]==1:
                del b[s2[i-1]]
            else:
                b[s2[i-1]]-=1
            b[s2[i + len(s1) - 1]] += 1
            if a==b:
                return True
        return False

            
        