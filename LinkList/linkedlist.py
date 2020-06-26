from typing import List
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def __repr__(self):
        return  f"Node({self.data})"

class LinkList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def get(self,index):
        current=self.head
        for i in range(1,index):
            current=current.next
        return current

    def insert(self,index,data):
        new_node=Node(data)
        if index<0 or index>self.size:
            raise Exception("索引越界")
        elif self.size==0:
             self.head=new_node
             self.tail=new_node
        elif index==1 and self.head is None:
            new_node.next=self.head
            self.head=new_node
        elif index==self.size:
            self.tail.next=new_node
            self.tail=new_node
        else:
            prev=self.get(index-1)
            new_node.next=prev.next
            prev.next=new_node
        self.size +=1


    def remove(self,index):
        current=self.head
        if current is None:
            raise Exception("空链表")
        elif index==1:
            self.head=current.next
        elif index==self.size:
            prev=self.get(index-1)
            current=prev.next
            prev.next=None
            self.tail=prev
        else:
            prev=self.get(index-1)
            # current=self.get(index)
            # prev.next= current.next
            current=prev.next
            prev.next= current.next
            # prev.next=prev.next.next
        self.size -=1
        return current
    def reversed(self):
        prev=None
        curr=self.head
        while curr:
            temp=curr.next
            if prev :
                curr.next=prev
            else:
                curr.next=prev
            prev=curr
            curr=temp
        self.head=prev


    def print_list(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next

    def __repr__(self):
        current=self.head
        string_list=""
        while current:
            string_list +=f"{current}-->"
            current=current.next
        return string_list +"end"

if __name__ == '__main__':
    ll=LinkList()
    ll.insert(0,1)
    ll.insert(1, 2)
    ll.insert(2, 3)
    ll.insert(3, 4)
    ll.insert(4, 5)
    print(ll.remove(1))
    print(ll.remove(2))
    print(ll.remove(3))
    print(ll)
    ll.reversed()
    print(ll)
    ll.print_list()

