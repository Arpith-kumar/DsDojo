"""
Description:
    - A circular linked list is a linked list where all nodes are connected to form a circle,
      there is no NULL at the end.
    - A circular linked list can be a singly circular linked list or a doubly circular linked list.

        first(head)              second                  third
            |                       |                      |
            |                       |                      |
        +------+-----+        +------+-----+        +------+------+
    --->| data |  o---------> | data |  o---------> | data |   o------>
    |   +------+-----+        +------+-----+        +------+------+   |
    |                                                                 |
    +-----------------------------------------------------------------+
"""

'''
The CircularLinkedListNode class defines the individual node in the linked list data structure.
'''


class CircularLinkedListNode:
    def __init__(self, data=None):
        # Data in the current node.
        self.data = data
        # Pointer to the next node.
        self.next = None


'''
The CircularLinkedList Class.
'''


class CircularLinkedList:

    def __init__(self):
        # Start with the head node - the first node in a LinkedList is called a the Head Node.
        self.head = None

    '''
    Inserts the values at the end of the LinkedList.
    '''

    def append(self, element):
        # Create a new node to be inserted.
        new_node = CircularLinkedListNode(element)
        # If LinkedList is empty just create a new head node and point it back to head.
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
            return
        # Else we iterate until we reach the end of the LinkedList (i.e until next of node is pointing to head)
        # and append the node to the end.
        current_node = self.head
        while current_node.next != self.head:
            current_node = current_node.next
        current_node.next = new_node
        # Also point the newly appended node to the head of the LinkedList.
        new_node.next = self.head

        '''
        Inserts the values at the beginning of the LinkedList.
        '''

    def prepend(self, element):
        # Create a new node to be inserted.
        new_node = CircularLinkedListNode(element)
        # Point the new node to the current head.
        new_node.next = self.head

        # Now to complete the circular connection.
        current_node = self.head
        # If the list is empty them point the new node to itself.
        if self.head is None:
            new_node.next = new_node
        else:
            # Else loop till the last element and the make a connection b/w the mast node and the
            # newly inserted head node.
            while current_node.next is not self.head:
                current_node = current_node.next
            current_node.next = new_node
        # All our connections are complete but we have not assigned the new node as head node yet.
        # So update the head as the new node just inserted to complete prepending.
        self.head = new_node

    def remove(self, element):
        current_node = self.head
        # When the element to be removed id present in the head node.
        if self.head.data == element:
            # Iterate till the last node and point the last node to the node next to the head.
            # Also assign the node next to the current head as new head.
            while current_node.next is not self.head:
                current_node = current_node.next
            current_node.next = self.head.next
            self.head = self.head.next
            return
        else:
            # For every other node do
            # In LinkedList the way we delete an element is by changing the pointers. What we do is once we find the
            # desired node to delete we skip the element to be deleted by pointing the previous element to the node
            # next to the element to be deleted.
            previous_node = None
            while current_node.next is not self.head:
                previous_node = current_node
                current_node = current_node.next
                if current_node.data == element:
                    previous_node.next = current_node.next
                    # current_node = current_node.next
                    return

        print(f'Element {element} not found in LinkedList.')
        return

    '''
    Prints all the elements in the LinkedList.
    '''

    def display(self):
        # Starting from the head node print the data of each node until you reach the end if the LinkedList.
        current_node = self.head
        if current_node is None:
            print('[ ]')
            return
        while current_node is not None:
            print(current_node.data, end=' -> ')
            current_node = current_node.next
            # CircularLinkedList breaking condition (End-of-list condition).
            if current_node == self.head:
                break
        print('pointer to head ' + str(self.head.data) if self.head else None)
        print()


if __name__ == "__main__":
    # Create a SinglyLinkedList Object
    circular_linked_list = CircularLinkedList()

    # Try out all the functions in the SinglyLinkedList class
    print('---------------------------------------------------------------------')
    print('Initial look at the LinkedList: ', end='')
    circular_linked_list.display()

    # NOTE that that the inputs are taken as comma seperated values.
    print('---------------------------------------------------------------------')
    elements_ = input('Enter the elements to be append into the LinkedList: ')
    elements_ = elements_.split(',')
    for element_ in elements_:
        circular_linked_list.append(element_)
    print('LinkedList after append: ', end='')
    circular_linked_list.display()

    # NOTE that that the inputs are taken as space seperated values.
    print('---------------------------------------------------------------------')
    elements_ = input('Enter the elements to be prepend into the LinkedList: ')
    elements_ = elements_.split(',')
    for element_ in elements_:
        circular_linked_list.prepend(element_)
    print('LinkedList after prepend: ', end='')
    circular_linked_list.display()

    print('\n---------------------------------------------------------------------')
    data_ = input('Enter element to be deleted: ')
    circular_linked_list.remove(data_)
    print('LinkedList after deletion: ', end='')
    circular_linked_list.display()
