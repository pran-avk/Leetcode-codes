class Solution(object):
    def lemonadeChange(self, bills):
        a={5:0,10:0,20:0}
        for i in bills:
            if i==5:
                a[5]+=1
            if i==10:
                a[10]+=1
                b=a.get(5,0)-1
                if b==-1:
                    return False
                else:
                    a[5]-=1
            if i==20:
                a[20]+=1
                b=a.get(10,0)
                c=a.get(5,0)
                if b>=1 and c>=1:
                    a[10]-=1
                    a[5]-=1
                elif c>=3:
                    a[5]-=3
                else:
                    return False
        return True
        