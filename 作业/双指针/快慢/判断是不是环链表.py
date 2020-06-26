
# 题目4:
# 判断链表有没有环
# 思考点:判断入环点在哪里
# #判断环长度

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def is_circle(head):
        solm=head
        fast=head
        while fast and fast.next:
            fast=fast.next.next
            solm=solm.next
            if solm==fast:
                return True
        return False


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node1.next=node2
    node2.next=node3
    node3.next=node4
    node4.next=node5
    node5.next=node6
    node6.next=node2
    print(is_circle(node1))



