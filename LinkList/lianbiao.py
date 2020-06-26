class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"

        # return "None({})".format(self.data)
        # return "None(%s)"%self.data


class LinkList:

    def __init__(self):
        self.head = None

    def insert_head(self, data):
        new_head = Node(data)
        if self.head:
            new_head.next = self.head
        self.head = new_head

    def print_List(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp=temp.next

    def __repr__(self):
        current = self.head
        string_repr = ""
        while current:
            string_repr += f"{current} --> "
            current = current.next
        return string_repr + "END"


if __name__ == '__main__':
    n = LinkList()
    n.insert_head(100)
    n.insert_head(99)
    n.insert_head(98)
    n.print_List()
    print(n)
