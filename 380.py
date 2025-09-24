class RandomizedSet:

    def __init__(self):
        self.lst = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.pos[val] = len(self.lst)
        self.lst.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        idx = self.pos[val]
        last = self.lst[-1]
        self.lst[idx] = last
        self.pos[last] = idx
        self.lst.pop()
        del self.pos[val]
        return True

    def getRandom(self) -> int:
        import random
        return random.choice(self.lst)


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print(obj.insert(1))
print(obj.remove(2))
print(obj.insert(2))
print(obj.getRandom())
print(obj.remove(1))
print(obj.insert(2))
print(obj.getRandom())
