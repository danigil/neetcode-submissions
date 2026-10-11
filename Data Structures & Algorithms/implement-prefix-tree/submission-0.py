# from collections import defaultdict
# from functools import partial

# dd_of_dd=partial(defaultdict, defaultdict)

class PrefixTree:

    def __init__(self):
        self.nodes={}

    def insert(self, word: str) -> None:
        chars=list(word)
        curr=self.nodes
        for c in chars:
            if c in curr:
                curr=curr[c]
            else:
                curr[c]={}
                curr=curr[c]
        curr['-']=True


    def search(self, word: str, withstop=True) -> bool:
        chars=list(word)
        if withstop:
            chars.append('-')
        curr=self.nodes
        for c in chars:
            if c not in curr:
                return False
            curr=curr[c]

        return True
        

    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix, withstop=False)
        
        