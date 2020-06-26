class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

    def __repr__(self):
        return f"Node({self.data})"

class LinkedQueue:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size = 0

    def is_empty(self):
        return self.tail is None

    def put(self,item):
        node=Node(item)
        if self.is_empty():
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
        self.size+=1

    def pop(self):
        if self.is_empty():
            raise Exception("get from empty queue")
        else:
            temp=self.head
            self.head=temp.next
        self.size-=1
        return temp

    def get(self,index):
        if self.is_empty():
            raise Exception("get from empty queue")
        else:
            n=0
            while n<index:
                temp = self.head
                self.head = temp.next
                n+=1
                self.size -= 1
            return temp

    def __repr__(self):
        curr=self.head
        string_queue=""
        while curr:
            string_queue+=f"{curr}<--"
            curr=curr.next
        return string_queue

if __name__ == '__main__':
    queue=LinkedQueue()
    queue.put(1)
    queue.put(2)
    queue.put(3)
    queue.put(4)
    queue.put(5)
    print(queue)
    print(queue.size)
    print(queue.get(3))
    queue.pop()
    print(queue)
    print(queue.size)
