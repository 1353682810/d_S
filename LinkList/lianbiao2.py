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
        new_head = Node(data)
        if self.head:
            new_head.next = self.head
        self.head = new_head

    def insert(self, i, data):
        if self.head is None or i == 1:
            self.insert_head(data)
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

    def append(self, data):
        if self.head is None:
            self.insert_head(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def linklist(self, obj: List):
        new_node = Node(obj[0])
        self.head = new_node
        current = self.head
        for i in obj[1:]:
            current.next = Node(i)
            current = current.next

    def delete(self):
        if self.head is None:
            print("空链表")
        else:
            self.head = self.head.next

    def pop(self):
        current = self.head
        if current is None:
            print("空链表")
        else:
            while current.next.next:
                current = current.next
            temp=current.next
            current.next = None
        return temp

    def delete_tail(self):
        if self.head is Node:
            print("空链表")
        else:
            current=self.head
            prev=current
            while current.next:
                prev = current
                current=current.next
            prev.next=None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def __repr__(self):
        current = self.head
        String_list = ''
        while current:
            String_list += f"{current}-->"
            current = current.next
        return String_list + 'end'


if __name__ == '__main__':
    ll = LinkList()
    # ll.insert_head(1)
    # ll.append(2)
    # ll.append(3)
    # ll.append(4)
    # ll.insert(2,3)
    ll.linklist([1, 2, 3, 4, 5, 6])
    ll.print_list()
    ll.delete_tail()
    # print(ll.pop())
    print("-------------------------------------")
    print(ll)
