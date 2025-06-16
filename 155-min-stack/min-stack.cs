public class MinStack {
    private Stack<(int value, int minSoFar)> stack;

    public MinStack() {
        this.stack=new Stack<(int,int)>();
    }
    
    public void Push(int val) {
        if (stack.Count == 0) {
            stack.Push((val, val));
        } 
        else{
            if(val<this.stack.Peek().minSoFar){
                this.stack.Push((val,val));
            }else{
                this.stack.Push((val,this.stack.Peek().minSoFar));
            }
        }
    }
    
    public void Pop() {
        this.stack.Pop();
    }
    
    public int Top() {
        return this.stack.Peek().value;
    }
    
    public int GetMin() {
        return this.stack.Peek().minSoFar;
        
    }
}
