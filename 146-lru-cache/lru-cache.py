class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.hashmap={}
        self.leftNode=Node(0,0)
        self.rightNode=Node(0,0)
        self.leftNode.next=self.rightNode
        self.rightNode.prev=self.leftNode

    #insert at end to list
    def insert(self,node):
        node.prev=self.rightNode.prev
        self.rightNode.prev.next=node
        self.rightNode.prev=node
        node.next=self.rightNode

    #delete from begining in the list
    def delete(self,node):
        node.next.prev=node.prev
        node.prev.next=node.next
        node.next=node.prev=None


    def get(self, key: int) -> int:
        if key in self.hashmap:
            #make it most recently used
            #delete and insert and add it to the end
            self.delete(self.hashmap[key])
            self.insert(self.hashmap[key])
            return self.hashmap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.delete(self.hashmap[key])
            node=Node(key,value)
            self.insert(node)
            self.hashmap[key]=node
        else:
            NewNode=Node(key,value)
            self.insert(NewNode)
            self.hashmap[key]=NewNode
            if len(self.hashmap)>self.capacity:
                node=self.leftNode.next
                self.delete(self.leftNode.next)
                del self.hashmap[node.key]
            




        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)