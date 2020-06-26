class Node:
    def __init__(self,data,next= None):
        self.data=data
        self.next=next

    def __repr__(self):
        return f"Node({self.data})"

class linkStack:
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
        self.size += 1



    def pop(self):
        if self.top is None:
            raise Exception("空")
        else:
            temp=self.top
            self.top=self.top.next
            self.size-=1
            return temp

    def is_empty(self):
        return self.top is None

    def print_stack(self):
        curr = self.top
        if self.top is None:
            raise Exception("空")
        else:
            while curr :
                print(curr.data)
                curr=curr.next


    def __repr__(self):
        if self.top is None:
            raise Exception("空")
        else:
            curr = self.top
            string_stack=""
            while curr:
                string_stack +=f"{curr}-->"
                curr = curr.next
            return  string_stack +"end"

if __name__ == '__main__':
    stack=linkStack()
    for i in range(5):
        stack.push(i)
    stack.print_stack()
    print(stack)
    print(stack.size)
    print(stack.pop())
    print(stack)
    print(stack.size)