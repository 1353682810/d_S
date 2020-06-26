class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return  f"node({self.data})"


class Linklist():
    def __init__(self):
        self.head = None

    def insert_h(self,data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        self.head = new_node


    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def __repr__(self):
        kt = self.head
        st = ""

        while kt:
            st +=f"{kt} - ->"
            kt = kt.next
        return st + "End"


    def append(self,data):#尾部插入
        if self.head is None:  #先判断有没有节点，没有的话调用insert_h
            self.insert_h(data)
        else:                   #有节点 self.head
            temp = self.head
            while temp.next:
                temp=temp.next
            temp.next=Node(data)


    def insert(self,i,data):
        if self.head is None or i==1:
             self.insert_h(data)
        else:
            new_node=Node(data)
            curr = self.head
            pre=curr
            j=1
            while j<i:
                pre=curr
                curr=curr.next
                j+=1
            pre.next=new_node
            new_node.next=curr
    def Linklist(self,seq):
        new_node=Node(seq[0])
        self.head=new_node
        curr=self.head
        for i in seq[1:]:
            curr.next=Node(i)
            curr=curr.next

    def delete_head(self):
        if self.head is None:
            print("空链表")
        else:
            self.head=self.head.next

    # def pop(self):
    #     curr = self.head
    #     if self.head is None:
    #         print("空链表")
    #     else:
    #
    #         while curr.next.next:
    #             curr=curr.next
    #         temp=curr.next.data
    #         curr.next=None
    #     return temp
    def pop(self):
        curr = self.head
        if self.head is None:
            print('空链表')
        else:
            while curr.next.next:
                curr = curr.next
            temp = curr.next.data
            curr.next = None
        return temp

    def delete_tail(self):
        if self.head is None:
            print("空链表")
        else:
            curr=self.head
            pre=curr
            while curr.next:
                pre=curr
                curr=curr.next
            temp=curr.data
            pre.next=None
        return temp








#if __name__ == '__main__':
   # s=Node(5)
   # print(s)

if __name__ == '__main__':
    l1=Linklist()
    # l1.insert_h(55)
    # l1.insert_h("da")
    # l1.insert_h(569)
    # l1.append(10)
    # l1.insert(3,1000000000)
    l1.Linklist([1,2,3,4,5,6,7,8,9])
    print(l1)
    # l1.delete_head()
    print(l1.pop())
    print(l1.pop())
    # print(l1.delete_tail())
    print("-------------")
    #l1.print_list()
    #print(l1)
    #print( l1.pop())
   # print(l1.delete_tail())
