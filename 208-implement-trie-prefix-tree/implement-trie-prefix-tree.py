class TreeNode:
    def __init__(self):
        self.children={}
        self.endOfWord=False

class Trie:

    def __init__(self):
        self.root=TreeNode()

    def insert(self, word: str) -> None:
        current=self.root
        for c in word:
            #if word[i] does not exists already - Add it to tree children
            if c not in current.children:
                # current=current.children[c]
                current.children[c] = TreeNode()
            #check if word[i] exists already
            current=current.children[c]
        #set end of word to True
        current.endOfWord=True

    def search(self, word: str) -> bool:
        current=self.root
        for c in word:
            if c not in current.children:
                return False
            current=current.children[c]
        if current.endOfWord==True: 
            return True
        else: return False
        
    def startsWith(self, prefix: str) -> bool:
        current=self.root
        for c in prefix:
            if c not in current.children:
                return False
            current=current.children[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)