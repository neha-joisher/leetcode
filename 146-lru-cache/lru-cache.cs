public class Node{
    public int val;
    public int key;
    public Node next;
    public Node prev;
    public Node(int key=0,int val=0, Node prev=null,Node next=null){
        this.key = key;
        this.val=val;
        this.prev=prev;
        this.next=next;
    }
}

public class LRUCache {
    private Dictionary<int,Node> keyToNode;
    private Node leftNode, rightNode;
    private int capacity;

    public LRUCache(int capacity) {
        this.keyToNode=new Dictionary<int,Node> ();
        this.capacity=capacity;

        this.leftNode=new Node();
        this.rightNode=new Node();
        this.leftNode.next=this.rightNode;
        this.rightNode.prev=this.leftNode;

    }

    public void Delete(Node key){
        Node temp=key.prev;
        key.prev.next=key.next;
        key.next.prev=temp;
        key.next=null;
        key.prev=null;
    }

    public void Insert(Node key){
        Node temp=this.rightNode.prev;
        this.rightNode.prev=key;
        key.next=this.rightNode;
        temp.next=key;
        key.prev=temp;
    }
    
    public int Get(int key) {

        //return the value if it exists
        if(this.keyToNode.ContainsKey(key)){
            //delete the node from LinkList
            Delete(this.keyToNode[key]);
            //insert at end- mark it as MRU
            Insert(this.keyToNode[key]);
            //return value
            return this.keyToNode[key].val;
        }

        //Return -1 if not
        return -1;
        
    }
    
    public void Put(int key, int value) {
        if (keyToNode.ContainsKey(key)) {
            Delete(keyToNode[key]);
            keyToNode.Remove(key);
        }

        Node newNode = new Node(key, value);
        Insert(newNode);
        keyToNode[key] = newNode;

        if (keyToNode.Count > capacity) {
            Node lru = leftNode.next; // least recently used
            Delete(lru);
            keyToNode.Remove(lru.key);
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.Get(key);
 * obj.Put(key,value);
 */