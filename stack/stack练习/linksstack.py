class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

    def __repr__(self):
        return f"Node({self.data})"

class LinkStack:
    def __init__(self):
        self.top=None
        self.size=0

    def push(self,itme):
        new_node=Node(itme)
        if self.top is None:
            self.top=new_node
        else:
            new_node.next=self.top
            self.top=new_node
        self.size+=1

    def pop(self):
        if self.top is None:
            raise Exception("空栈")
        else:
            temp=self.top
            self.top=self.top.next
            self.size-=1
            return temp

    def peek(self):
        if self.top is None:
            raise Exception("空栈")
        else:
            return  self.size

    def is_empty(self):
        return self.top is None

    def __repr__(self):
        curr=self.top
        string=""
        while curr:
            string+=f"{curr}-->"
            curr=curr.next
        return string+"end"
if __name__ == '__main__':
    stack1=LinkStack()
    for i in range(5):
        stack1.push(i)
    print(stack1)
    print(stack1.peek())
    print(stack1.pop())
    print(stack1)
    print(stack1.peek())