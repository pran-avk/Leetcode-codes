class Solution(object):
    def isValid(self, s):
        if len(s)%2!=0:
            return False
        a=[]
        for i in s:
            if i=='(':
                a.append(')')
            elif i=='[':
                a.append(']')
            elif i=='{':
                a.append('}')
            else:
                if a:
                    b=a.pop()
                    if b!=i:
                        return False
                else:
                    return False
        return not a
        