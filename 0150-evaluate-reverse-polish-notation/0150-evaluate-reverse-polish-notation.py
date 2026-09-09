class Solution(object):
    def evalRPN(self, tokens):
        a=[]
        for i in tokens:
            if i.lstrip("-").isdigit():
                a.append(int(i))
            elif i=="+":
                b=a.pop()
                c=a.pop()
                a.append(b+c)
            elif i=="*":
                b=a.pop()
                c=a.pop()
                a.append(b*c)
            elif i=="-":
                b=a.pop()
                c=a.pop()
                a.append(int(c-b))
            elif i=="/":
                b=a.pop()
                c=a.pop()
                result = abs(c) // abs(b)
                if c * b < 0:
                    result = -result
                a.append(result)
        return a[-1]

        