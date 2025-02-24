class TrieNode:
    def __init__(self):
        self.children={}
        self.endOfWord=False

class PrefixTree:
        def __init__(self):
            self.root=TrieNode()

        def insert(self,word):
            current=self.root
            for c in word:
                if c not in current.children:
                    current.children[c]=TrieNode()
                current=current.children[c]
            current.endOfWord=True
        
        def countOfLongestPrefix(self):
            current=self.root
            str_prefix=""
            while True:
                # If there are no children or it's the end of a word, stop
                if len(current.children) != 1 or current.endOfWord:
                    break
                for c in current.children:
                    str_prefix += c  # Add that character to the prefix
                    current = current.children[c]  
            return str_prefix


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        p=PrefixTree()
        for s in strs:
            p.insert(s)
        if len(p.root.children) >=2: return ""
        else: return p.countOfLongestPrefix()
            





        