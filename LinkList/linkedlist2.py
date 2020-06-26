"""
:Author:  Mr.Fang
:Create:  2020/6/23 22:22
:Github:  https://github.com/WeaponMaster
Copyright (c) 2020, Mr.Fang Group All Rights Reserved.
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return f"Node({self.data})"

class LinkList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def get(self,index):
        curr=self.head
        for i in range(1,index):
            curr=curr.next
        return curr
    def insert(self,index,element):
        new_node=Node(element)
        if index<0 or index>self.size:
            raise Exception("索引越界")
        elif self.size==0:
            self.head=new_node
            self.tail=new_node
        elif index==1 and self.head is  None:
            new_node.next=self.head
            self.head=new_node
        elif index==self.size:
            self.tail.next=new_node
            self.tail=new_node
        else:
            curr=self.get(index-1)
            curr.next=new_node
            new_node.next=curr.next.next
        self.size+=1

    def remove(self,index):
        if index<0 or index>self.size:
            print("索引越界")
        elif self.head is None:
            print("空链表")
        elif index==1:
            self.head=self.head.next
        elif index==self.size:
            curr=self.get(self.size-1)
            self.tail=curr
        else:
            prev=self.get(index-1)
            curr=prev.next
            prev.next=curr.next
        self.size -=1
    def reverse(self):
        prev=None
        curr=self.head
        while curr:
            temp=curr.next
            if prev:
                curr.next=prev
            else:
                curr.next=prev
            prev=curr
            curr=temp
        self.head=prev

    def print_list(self):
        curr=self.head
        while curr:
            print(curr.data)
            curr=curr.next

    def __repr__(self):
        curr=self.head
        string=""
        while curr:
            string +=f"{curr}-->"
            curr=curr.next
        return string+ "end"
if __name__ == '__main__':
    ll=LinkList()
    ll.insert(0,1)
    ll.insert(1,2)
    ll.insert(2,3)
    ll.insert(3,4)
    ll.insert(4,5)
    ll.insert(5,6)
    ll.remove(1)
    ll.remove(2)
    ll.remove(4)
    print(ll)
    ll.reverse()
    print(ll)
    ll.print_list()