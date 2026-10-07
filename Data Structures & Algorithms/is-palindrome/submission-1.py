class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s_l = []
        for c in s:
            if ord(c) in range(ord('a'), ord('z')) or ord(c) in range(ord('A'), ord('Z')) or ord(c) in range(ord('0'), ord('9')):
                new_s_l.append(c.lower())

        s="".join(new_s_l)
        # print(s)
        
        l=0
        r=len(s)-1

        while 0 <= l < r < len(s):
            if s[l] != s[r]:
                return False

            l+=1
            r-=1
        
        return True