class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.pos = {} 

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.pos:
            idx = self.pos[val]
            le = self.nums[-1] # get last element from list
            self.nums[idx] = le
            self.pos[le] = idx
            self.nums.pop()
            del self.pos[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        #return self.nums[random.randint(0, len(self.nums) - 1)]
        return random.choice(self.nums)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
