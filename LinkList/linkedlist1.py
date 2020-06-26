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
        current=self.head
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
            prev.next=new_node
            new_node.next=prev.next
        self.size +=1

    def remove(self,index):
        if self.head is None:
            raise Exception('空链表')
        elif index<0 and index>self.size:
            raise Exception('越界')
        elif index==1:
            self.head=self.head.next
        elif index==self.size:
            curr=self.get(self.size-1)
            self.tail=curr
        else:
            prev=self.get(index-1)
            curr=prev.next
            prev.next=curr.next

    def reverse(self):
        prev=None
        curr=self.head
        while curr:
            temp=curr.next
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
        string_list=''
        while curr:
            string_list +=f"{curr}-->"
            curr=curr.next
        return string_list + "end"

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