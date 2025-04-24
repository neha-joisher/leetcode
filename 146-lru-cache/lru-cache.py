class Node:
    def __init__(self,key=0,val=0, next=None,prev=None):
        self.key=key
        self.val=val
        self.prev=prev
        self.next=next

class LRUCache:

    def __init__(self, capacity: int):
        self.cache={}
        self.capacity=capacity
        self.left=self.right=Node()
        self.left.next,self.right.prev=self.right,self.left

    def get(self, key: int) -> int:
        if key in self.cache:

            #make it most recently used
            self.delete(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].val
        return -1

    #delete using the key
    def delete(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev

    #delete at end using key
    def insert(self,node):
        node1=self.right.prev
        node1.next=node
        node.prev=node1
        self.right.prev=node
        node.next=self.right


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
        node=Node(key,value)
        self.insert(node)
        self.cache[key]=node
        if len(self.cache)>self.capacity:
            key1=self.left.next.key
            self.delete(self.left.next)
            del self.cache[key1]



        
