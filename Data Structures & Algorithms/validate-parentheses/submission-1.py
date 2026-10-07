class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        # print(s)
        # curr = None
        opening = {
            '(':')',
            '{':'}',
            '[':']'
        }

        closing = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        st=[]

        for c in s:
            if c in opening:
                curr_exp_close = opening[c]
                st.append(curr_exp_close)
            else:
                if len(st)==0 or st.pop()!=c:
                    # print(c)
                    # print(st)
                    return False

        if len(st)>0:
            return False

        return True