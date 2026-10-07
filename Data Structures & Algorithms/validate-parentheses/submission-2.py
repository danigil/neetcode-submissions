class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        opening = {
            '(':')',
            '{':'}',
            '[':']'
        }

        st=[]

        for c in s:
            if c in opening:
                curr_exp_close = opening[c]
                st.append(curr_exp_close)
            else:
                if len(st)==0 or st.pop()!=c:
                    return False

        if len(st)>0:
            return False

        return True