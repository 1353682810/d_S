class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class LinkList:

    def __init__(self):
        self.head=None

    def insert_head(self, data):
        new_head = Node(data)
        if self.head:
            new_head.next = self.head
        self.head = new_head

    def append(self,data):
        if self.head is None:
            self.insert_head(data)
        else:
            current=self.head
            while current.next:
                    current=current.next
            current.next=Node(data)


    def print_List(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def __repr__(self):
        current = self.head
        String_List = ''
        while current:
            String_List += f"{current}-->"
            current = current.next
        return String_List + 'end'


if __name__ == '__main__':
    ll = LinkList()
    ll.insert_head(100)
    ll.append(99)
    ll.append(98)
    ll.print_List()
    print("----------------------")
    print(ll)
