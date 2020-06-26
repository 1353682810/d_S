from typing import List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class LinkList:
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.insert_head()
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert(self, i, data):
        if self.head is None or i == 1:
            self.insert_head()
        else:
            new_node = Node(data)
            current = self.head
            prev = current
            j = 1
            while j < i:
                prev = current
                current = current.next
                j += 1
            prev.next = new_node
            new_node.next = current

    def delete(self):
        if self.head is None:
            print("空链表")
        else:
            self.head = self.head.next

    def pop(self):
        if self.head is None:
            print("空链表")
        else:
            current = self.head
            while current.next:
                prve=current
                current = current.next
            temp = current
            prve.next = None
            return temp

    def delete_tail(self):
        if self.head is None:
            print("空链表")
        else:
            current = self.head
            prev = current
            while current.next:
                prev = current
                current = current.next
            temp = prev.next
            prev.next = None
            return temp

    def linklist(self,obj: List):
        new_node=Node(obj[0])
        self.head=new_node
        current=self.head
        for i in obj[1:]:
            current.next=Node(i)
            current=current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def __repr__(self):
        current = self.head
        string_list = ''
        while current:
            string_list += f"{current}-->"
            current = current.next
        return string_list + "end"


if __name__ == '__main__':
    ll = LinkList()
    # ll.insert_head(1)
    # ll.append(2)
    # ll.append(3)
    # ll.append(4)
    # ll.append(5)
    # ll.insert(2, 6)
    ll.linklist([1,2,3,4,5,6])
    ll.delete()
    print(ll.pop())
    # ll.delete_tail()
    ll.print_list()
    print("-------" * 5)
    print(ll)
