class RandomizedSet:

    def __init__(self):
        self.data=[]
        self.indices={}
        
    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        else:
            index=len(self.data)
            self.indices[val]=index
            self.data.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        else:
            # Find index of val and get the last element
            index = self.indices[val]
            last_element = self.data[-1]

            # Swap val with the last element in O(1)
            self.data[index] = last_element
            self.indices[last_element] = index

            # Remove the last element from data and delete val from indices
            self.data.pop()
            del self.indices[val]
            return True

    def getRandom(self) -> int:
        return random.choice(self.data)
        

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()