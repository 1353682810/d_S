from typing import List
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return f"(Node{self.data})"

class Linklist:
    def __init__(self):
        self.head=None

    def insert_head(self,data):
        new_head=Node(data)
        if self.head:
            self.head.next=self.head
        self.head=new_head

    def append(self,data):
        if self.head is None:
            self.insert_head()
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=Node(data)

    def insert(self,i,data):
        if self.head is None or i==1:
            self.insert_head()
        else:
            new_node=Node(data)
            current=self.head
            prev=current
            j=1
            while j<i:
                prev=current
                current=current.next
                j+=1
            prev.next=new_node
            new_node.next=current

    def delete(self):
        if self.head is None:
            print("空链表")
        else:
            self.head=self.head.next
    def pop(self):
        if self.head is None:
            print("空链表")
        else:
            current=self.head
            while current.next.next:
                current = current.next
            temp=current.next
            current.next = None
            return temp
    def delect_tail(self):
        if self.head is None:
            print("空链表")
        else:
            current=self.head
            prev=current
            while current.next:
                prev=current
                current=current.next
            temp=current
            current=Node
            return  temp
    def delect_index(self,i):
        if self.head is None:
            print("空链表")
        elif i==1:
            self.delete()
        else:
            current=self.head
            prev=current
            j=1
            while j<i:
                prev=current
                current= current.next
                j+=1
            prev.next=current.next

    def linklist(self,obj: List):
        new_node=Node(obj[0])
        self.head=new_node
        current=self.head
        for i in obj[1:]:
            current.next=Node(i)
            current=current.next

    def print_list(self):
        new_head=self.head
        while new_head:
            print(new_head.data)
            new_head=new_head.next


    def __repr__(self):
        current=self.head
        string_list=''
        while current:
            string_list+=f"{current}-->"
            current=current.next
        return string_list +"end"

if __name__ == '__main__':
    ll=Linklist()
    # ll.insert_head(1)
    # ll.append(2)
    # ll.append(3)
    # ll.append(4)
    # ll.insert(2,5)
    ll.linklist([1,2,3,4,5])
    ll.delete()
    ll.delect_index(3)
    ll.print_list()
    print("----------------")
    print(ll)