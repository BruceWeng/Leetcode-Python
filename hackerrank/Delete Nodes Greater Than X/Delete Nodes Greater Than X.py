'''
Complete the removeNodes function provided in your editor. It has 2 parameters:

1. list: A reference to a Linked List Node that is the head of a linked list.
2. x: An integer value.

Your funciton should remove all nodes from the list having data values greater than x, and then return the head of the modified linked list.

Input Format
The locked stub code in your editer processes the following inputs and pased the necessary arguments to the removeNodes function:
The first line contains N, the number of nodes in the linked list.
Each line i (where 0<= i <) of the N subsequent lines contains an integer representing the value of a node in the linked list. The last line contains an integer, x.

Output Format
Return the linked list after removing the nodes containing values > x.

Sample Input 1:
5
1
2
3
4
5
3

Sample Output 1:
1
2
3

Sample Input 2:
5
5
2
1
6
7
5

Sample Output2:
5
2
1
'''

class LinkedListNode:
    def __init__(self, node_Value):
        self.val = node_Value
        self.next = None

def _insert_node_into_singlylinkedlist(head, tail, val):
    if head == None:
        head = LinkedListNode(val)
        tail = head
    else:
        node = LinkedListNode(val)
        tail.next = node
        tail = tail.next

def  removeNodes(list, x):
    if list == None or x == None:
        return None
    temp = list
    while temp.val > x:
        temp = temp.next

    curr = temp
    prev = None
    while curr != None:
        if curr.val > x:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next

    return temp
