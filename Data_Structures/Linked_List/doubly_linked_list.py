'''
The DoublyLinkedListNode class defines the individual node in the linked list data structure.
'''


class DoublyLinkedListNode:
    def __init__(self, data=None):
        # Data in the current node.
        self.data = data
        # Pointer to the next node.
        self.next = None
        # Pointer to the previous node.
        self.prev = None


'''
The DoublyLinkedList Class.
'''


class DoublyLinkedList:

    def __init__(self):
        # Start with the head node - the first node in a LinkedList is called a the Head Node.
        self.head = None
    
    '''
    Inserts the values at the end of the LinkedList.
    '''

    def append(self, element):
        # Create a new node to be inserted.
        new_node = DoublyLinkedListNode(element)
        # If list empty
        if self.head is None:
            # Head node's prevoius points to None.
            new_node.prev = None
            self.head = new_node
        else:
        # If atleast one node present
            current_node = self.head
            # Iterate to the last node of the list 
            while current_node.next is not None:
                current_node = current_node.next
            # Point the current last node to the new last node 
            current_node.next = new_node
            # Point the previous pointer of the new last node to the current last node.
            new_node.prev = current_node
            # Point the next pointer of the new last node to None.
            new_node.next = None
            
        

    '''
    Inserts the values at the beginning of the LinkedList.
    '''

    def prepend(self, element):
        # Create a new node to be inserted.
        new_node = DoublyLinkedListNode(element)
        # If list empty
        if self.head is None:
            # Head node's prevoius points to None.
            new_node.prev = None
            self.head = new_node
        else:
        # If atleast one node present
            # Point the new node's next pointer to the current head.
            new_node.next = self.head
            # Point the new nodes previous pointer to None.
            new_node.prev = None
            # Point the current heads previous pointer to the new node.
            self.head.prev = new_node
            # Assign the new node as the new head.
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
        new_node = DoublyLinkedListNode(element)
        idx = 0
        current_node = self.head

        # If the insertion is to be done at the end according to the index then just call the append function.
        if index == self.length() - 1:
            self.append(element)
            return
        else:
            # For ever other index value.
            # current_node is the node after which the new element is to be added, next_node is the node that has to be
            # present next to the new_node after insertion.
            # First we identify the node after which we have to do the insertion, then we do some modifications in the connection
            # between these nodes.
            while current_node is not None:
                next_node = current_node.next
                if idx == index:
                    current_node.next = new_node
                    new_node.next = next_node

                    next_node.prev = new_node
                    new_node.prev = current_node
                idx += 1
                current_node = current_node.next
            return
    
    '''
    Delete a value after the specified index.
    '''

    def delete_after(self, index):
        # Check whether the index given is a vaild index for this LinkedList.
        if index < 0 or index >= self.length() - 1:
            print(f"IndexError: No Node in LinkedList after index {index}")
            return
        idx = 0
        current_node = self.head

        # If you want to delete the last node.
        if index == self.length() - 2:
            # Iterrate to the last node in the list, come back one node and de-linke and delete the last node.
            while current_node.next is not None:
                current_node = current_node.next
            new_tail_node = current_node.prev
            new_tail_node.next = None

            current_node.prev = None
            current_node.data = None
            return
        # For every other node.
        else:
            # Here next_node is the node next to the node that has to be deleted.
            # Once we reach the node after which we have to delete a node(current_node), we delink the node to the deleted by making,
            # connections between the current_node and the next_node.
            while current_node.next is not None:
                next_node = current_node.next.next
                if idx == index:
                    current_node.next = next_node
                    next_node.prev = current_node
                # Move forward in the list.
                idx += 1
                current_node = current_node.next
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
            print(current_node.data, end=' <-> ')
            current_node = current_node.next
        print('null')
        print()

if __name__ == "__main__":
    # Create a DoublyLinkedList Object
    doubly_linked_list = DoublyLinkedList()

    # Try out all the functions in the SinglyLinkedList class
    print('---------------------------------------------------------------------')
    print('Initial look at the LinkedList: ', end='')
    doubly_linked_list.display()

    # NOTE that that the inputs are taken as comma seperated values.
    print('---------------------------------------------------------------------')
    elements_ = input('Enter the elements to be append into the LinkedList: ')
    elements_ = elements_.split(',')
    for element_ in elements_:
        doubly_linked_list.append(element_)
    print('LinkedList after append: ', end='')
    doubly_linked_list.display()

    # NOTE that that the inputs are taken as space seperated values.
    print('---------------------------------------------------------------------')
    elements_ = input('Enter the elements to be prepend into the LinkedList: ')
    elements_ = elements_.split(',')
    for element_ in elements_:
        doubly_linked_list.prepend(element_)
    print('LinkedList after prepend: ', end='')
    doubly_linked_list.display()

    print('---------------------------------------------------------------------')
    print('Length of LinkedList: ', str(doubly_linked_list.length()))
    
    print('\n---------------------------------------------------------------------')
    print('Insert after index: ')
    index_ = int(input('Index: '))
    data_ = input('Element: ')
    doubly_linked_list.insert_after(index_, data_)
    print('LinkedList after insertion: ', end='')
    doubly_linked_list.display()

    print('\n---------------------------------------------------------------------')
    index_ = int(input('Delete after index: '))
    doubly_linked_list.delete_after(index_)
    print('LinkedList after deletion: ', end='')
    doubly_linked_list.display()