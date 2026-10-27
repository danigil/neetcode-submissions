class RandomizedSet:

    def __init__(self):
        self.l=[]
        self.d=dict()

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.d[val]=len(self.l)
        self.l.append(val)
        return True


    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False
        # print(self.l)
        # print(self.d)
        last = self.l[-1]
        idx = self.d[val]
        self.d[last]=idx
        self.l[idx]=last
        self.l.pop()
        del self.d[val]

        return True


    def getRandom(self) -> int:
        idx = random.randint(0, len(self.l)-1)
        return self.l[idx] 


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()