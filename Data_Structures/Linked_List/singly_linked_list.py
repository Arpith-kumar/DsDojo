"""
Description:
    - A linked list is a linear collection of data elements, whose order is not given by their physical
      placement in memory.
    - Instead, each element points to the next.
    - It is a data structure consisting of a collection of nodes that together represent a sequence.

        first(head)              second                  third
            |                       |                      |
            |                       |                      |
        +------+-----+        +------+-----+        +------+------+
        | data |  o-------->  | data |  o-------->  | data | None |
        +------+-----+        +------+-----+        +------+------+
"""

'''
The SinglyLinkedListNode class defines the individual node in the linked list data structure.
'''


class SinglyLinkedListNode:
    def __init__(self, data=None):
        # Data in the current node.
        self.data = data
        # Pointer to the next node.
        self.next = None


'''
The SinglyLinkedList Class.
'''


class SinglyLinkedList:
    def __init__(self):
        # Start with the head node - the first node in a LinkedList is called a the Head Node.
        self.head = None

    '''
    Inserts the values at the end of the LinkedList.
    '''

    def append(self, element):
        # Create a new node to be inserted.
        new_node = SinglyLinkedListNode(element)
        # If the LinkedList is empty we simple assign the new node as the new head of the LinkedList.
        if self.head is None:
            self.head = new_node
            return
        # Else we iterate until we reach the end of the LinkedList and append the node to the end.
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    '''
    Inserts the values at the beginning of the LinkedList.
    '''

    def prepend(self, element):
        # Create a new node to be inserted.
        new_node = SinglyLinkedListNode(element)
        # Point the new node to the current head.
        new_node.next = self.head
        # Then update the head as the new node just inserted to complete prepending.
        self.head = new_node

    '''
    Finds the length of the LinkedList.
    '''

    def length(self):
        # We start from the top of the LinkedList
        current_node = self.head
        count = 0
        # We count the length of the LinkedList by counting the no.of nodes in it. Traverse through the LinkedList
        # and increment count until you find the last node (i.e: when a node points to null)
        while current_node is not None:
            count += 1
            current_node = current_node.next
        # Return the lenght of the LinkedList
        return count

    '''
    Inserts a value after the specified index.
    '''

    def insert_after(self, index, element):
        # Check whether the index given is a vaild index for this LinkedList.
        if index < 0 or index > self.length():
            print("IndexError: LinkedList index out of range")
            return
        new_node = SinglyLinkedListNode(element)
        idx = 0
        current_node = self.head
        # Point the previous node to the new node
        # Then point the new node to the next node to complete insertion.
        while current_node is not None:
            # previous_node is the node after which the insertion should take place
            previous_node = current_node
            # current_node is the node on the right of the newly inserted node.
            current_node = current_node.next
            if index == idx:
                previous_node.next = new_node
                new_node.next = current_node
            idx += 1
    
    '''
    Deletes node by index value.
    '''

    def remove_byindex(self, index):
        # Check whether the index given is a valid index for this LinkedList.
        if index < 0 or index > self.length() - 1:
            print("IndexError: LinkedList index out of range")
            return

        current_node = self.head
        # If the desired index is 0 then simply assign the 2nd element in the list as new head node.
        # Also set the current head to be None(null).
        if current_node and index == 0:
            self.head = current_node.next
            current_node = None
            return

        # Initialize another index-variable i for comparision with index
        idx = 0
        # In LinkedList the way we delete an element is by changing the pointers. What we do is once we find the
        # desired index to delete we skip the element to be deleted by pointing the previous element to the node
        # next to the element to be deleted.
        previous_node = None
        while current_node is not None and idx != index:
            idx += 1
            previous_node = current_node
            current_node = current_node.next

        # if current_node is not None:
        previous_node.next = current_node.next
        current_node = None
        return

    '''
    Deletes node by element value.
    '''

    def remove_byvalue(self, element):
        current_node = self.head
        # If the desired element is present in the head node itself then simply assign the 2nd element in the list as
        # head. Also set the current head to be None(null).
        if current_node and current_node.data == element:
            self.head = current_node.next
            current_node = None
            return

        # In LinkedList the way we delete an element is by changing the pointers. What we do is once we find the
        # desired node to delete we skip the element to be deleted by pointing the previous element to the node
        # next to the element to be deleted.
        previous_node = None
        while current_node is not None and current_node.data != element:
            previous_node = current_node
            current_node = current_node.next

        # If you have not reached the last node continue the deletion process...
        if current_node is not None:
            previous_node.next = current_node.next
            current_node = None
            return

        print(f'Element {element} not found in LinkedList.')
        return

    '''
    Reverse the given LinkedList.
    '''

    def reverse(self):

        # node1 -> node2 -> node3 -> node4 - null
        # node4 -> node3 -> node2 -> node1 - null
        # null <- node4 <- node3 <- node2 <- node1
        # So basically what we do to reverse a LinkedList is reverse it's pointer and reassign it's head position.
        previous_node = None
        current_node = self.head

        while current_node is not None:
            # We save the next node pointer in a temp variable.
            temp = current_node.next
            # We flip the pointer in the opposite direction.
            current_node.next = previous_node

            # Update our previous node to current node for next itteration
            previous_node = current_node
            # We update the current node pointer with the saved value in the temp variable. We do the saving of the
            # pointer because we want to move forward in the list to flip the pointers of all the nodes. If we do not
            # save the current nodes original pointer we will not be able to progress forward in this list.
            current_node = temp

        # Once the above while loop finishes the previous_node variable will be pointing at the last node in the list.
        # Since we want to reverse the list we reassign head to point to the last element of the list.
        # Our LinkedList should look somthing like this at this point.
        # null <- node4 <- node3 <- node2 <- node1 <= head-pointer
        self.head = previous_node

    '''
    Prints all the elements in the LinkedList.
    '''

    def display(self):
        # Starting from the head node print the data of each node until you reach the end if the LinkedList.
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=' -> ')
            current_node = current_node.next
        print('null')
        print()


if __name__ == "__main__":
    # Create a SinglyLinkedList Object
    singly_linked_list = SinglyLinkedList()

    # Try out all the functions in the SinglyLinkedList class
    print('---------------------------------------------------------------------')
    print('Initial look at the LinkedList: ', end='')
    singly_linked_list.display()

    # NOTE that that the inputs are taken as comma seperated values.
    print('---------------------------------------------------------------------')
    elements_ = input('Enter the elements to be append into the LinkedList: ')
    elements_ = elements_.split(',')
    for element_ in elements_:
        singly_linked_list.append(element_)
    print('LinkedList after append: ', end='')
    singly_linked_list.display()

    # NOTE that that the inputs are taken as space seperated values.
    print('---------------------------------------------------------------------')
    elements_ = input('Enter the elements to be prepend into the LinkedList: ')
    elements_ = elements_.split(',')
    for element_ in elements_:
        singly_linked_list.prepend(element_)
    print('LinkedList after prepend: ', end='')
    singly_linked_list.display()

    print('---------------------------------------------------------------------')
    print('Length of LinkedList: ', str(singly_linked_list.length()))

    print('\n---------------------------------------------------------------------')
    print('Insert after an index: ')
    index_ = int(input('Index: '))
    data_ = input('Element: ')
    singly_linked_list.insert_after(index_, data_)
    print('LinkedList after insertion: ', end='')
    singly_linked_list.display()

    print('\n---------------------------------------------------------------------')
    data_ = input('Enter element to be deleted: ')
    singly_linked_list.remove_byvalue(data_)
    print('LinkedList after deletion: ', end='')
    singly_linked_list.display()

    print('\n---------------------------------------------------------------------')
    index_ = int(input('Enter index of element to be deleted: '))
    singly_linked_list.remove_byindex(index_)
    print('LinkedList after deletion: ', end='')
    singly_linked_list.display()

    print('\n---------------------------------------------------------------------')
    print('Reversing a LinkedList')
    print('LinkedList before reversal: ', end='')
    singly_linked_list.display()
    singly_linked_list.reverse()
    print('LinkedList after reversal: ', end='')
    singly_linked_list.display()
