#Linked List

"""
An object for storing a single node of a linked list.
Models two attributes - data and the link to the next node in the list
"""

###---###

#Singly Linked List

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None

class LinkedList:
    """
    Linear data structure that stores values in nodes.
    """

    def __init__(self):
        self.head = Node()


    def is_empty(self):
        return self.head is None #Checks if empty


    def size(self):
        """
        Returns the number of nodes in the list
        Takes O(n) time (Linear)
        """

        current = self.head
        count = 0 #Increments everytime you visit a node

        while current != None:
            count += 1
            current = current.next_node

        return count


    def append(self, data):
        """
        Adds new Node containing data at head of the list
        Takes constant time O(1)
        """
        new_node = Node(data)
        current = self.head
        while current.next_node != None:
            current = current.next_node
        current.next_node = new_node

    def set(self, index, data):
        current = self.head
        current_index = 0
    
        if index >= self.size() or index < 0:
            return self.append(data)
        
        while current:
            if index == current_index:
                current.data = data
                return
            else:
                current_index += 1
                current = current.next_node

    def search_value(self, key):
        """
        Search method to match query
        Returns the node or if not found "None"
        Linear time O(n)
        """

        current = self.head
        index = 0

        while current:
            if current.data == key: #If target matches key, then returns current
                str = "Key value {} found at index: {}".format(key, index)
                return str
            else:
                index += 1
                current = current.next_node

        return None
        
    
    def get_index(self, index):
        """
        Search method to find value at position index
        """
        
        current = self.head
        current_index = 0
        
        while current:
            if index == current_index:
                str = "Key value {} found at index: {}".format(current.data, index)
                return str
            else:
                current_index += 1
                current = current.next_node
        
        return None


    def insert(self, data, index):
        """
        Inserts a new Node containing data at index position
        Insertion takes constant O(1) but finding node takes linear time O(n)
        """
        
        current = self.head
        previous_node = self.head
        current_index = 0

        if index >= self.size() or index < 0:
            return self.append(data)

        while True:
            current = current.next_node
            if index == current_index:
                new_node = Node(data)
                previous_node.next_node = new_node
                new_node.next_node = current
                return
            else:
                current_index += 1
                previous_node = current


    def remove_value(self, key):
        """
        Removes Node containing data that matches the key
        Returns the Node or None if key doesn't exist
        Takes linear time O(n) 
        """

        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current == self.head:
                found = True
                self.head = current.next_node
            
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            
            else:
                previous = current
                current = current.next_node

        return current

    def remove_index(self, index):
        current = self.head
        current_index = 0

        if index >= self.size() or index < 0:
            return
        
        while True:
            previous_node = current
            current = current.next_node
            if index == current_index:
                previous_node.next_node = current.next_node
                return
            else:
                current_index += 1                
    
    def display(self):
        """
        Prints all nodes elements
        """
        
        elements = []
        current = self.head
        
        while current.next_node != None:
            current = current.next_node
            elements.append(current.data)
        print(elements)


    def __repr__(self):
        """
        Returns a string representation of the list
        Takes Linear time O(1)
        """

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
                
            current = current.next_node

        return '--> '.join(nodes)
