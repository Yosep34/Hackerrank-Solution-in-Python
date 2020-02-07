

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_node_at_the_end(self, data):
        newNode = Node(data)
        if (self.head):
            last = self.head
            while last.next:
                last = last.next
            last.next = newNode
        else:
            self.head = newNode

def printLinkedList(head):
    while head is not None:
        print(head.data)
        head = head.next

if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node_at_the_end(llist_item)

    printLinkedList(llist.head)