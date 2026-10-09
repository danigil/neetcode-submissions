class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l=[]
        ops = {
            "+": lambda x,y: x+y,
            "*": lambda x,y: x*y,
            "-": lambda x,y: y-x,
            "/": lambda x,y: int(float(y) / x),
        }
        i=0
        for token in tokens:
            curr_op = ops.get(token)
            # print(l)
            if curr_op is not None:
                n1,n2=l.pop(), l.pop()
                l.append(curr_op(n1,n2))
                if i==1:
                    i+=1
                else:
                    i+=1
            else:
                l.append(int(token))
        
        return l[0]
