
class Node:
    def __init__(self,item):
        self.item=item
        self.next=None

class LinkedList:

    def __init__(self):
        self.head=None

if __name__=='__main__':
    linked_list=LinkedList()
    # assign item values
    linked_list.head=Node(1)
    second=Node(2)
    third=Node(3)

    # connect nodes
    linked_list.head.next=second
    second.next=third

    # print the items
    while linked_list.head != None:
        print(linked_list.head.item, end=" ")
        linked_list.head = linked_list.head.next