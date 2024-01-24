#!/usr/bin/python3
"""Node
"""


class Node:
    """A class representing a node in a singly linked list.

    Attributes:
        data (int): The data stored in the node.
        next_node (Node or None): Reference to the next node in the list.
    """

    def __init__(self, data, next_node=None):
        """Initialize a node with the given data and next_node.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node or None): The next node in the linked list.
            Defaults to None.

        Raises:
            TypeError: If data is not an integer or next_node is
            not a Node object or None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method for the data attribute.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method for the data attribute.

        Args:
            value (int): The data to be stored in the node.

        Raises:
            TypeError: If the provided value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter method for the next_node attribute.

        Returns:
            Node or None: The next node in the linked list or
            None if there is no next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method for the next_node attribute.

        Args:
            value (Node or None): The next node in the linked list or None.

        Raises:
            TypeError: If value is not a Node object or None.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object or None")
        self.__next_node = value


"""single linked list

"""


class SinglyLinkedList:
    """A class representing a singly linked list.

    Attributes:
        head (Node): The head node of the linked list.
    """

    def __init__(self):
        """Initialize an empty singly linked list."""
        self.head = None

    def __str__(self):
        """Return a string representation of the linked list.

        Returns:
            str: A string representation of the linked list.
        """
        rtn = ""
        ptr = self.head

        while ptr is not None:
            rtn += str(ptr.data)
            if ptr.next_node is not None:
                rtn += "\n"
            ptr = ptr.next_node

        return rtn

    def sorted_insert(self, value):
        """Insert a new node with the given value in sorted order.

        Args:
            value (int): The value to be inserted into the linked list.
        """
        ptr = self.head

        while ptr is not None:
            if ptr.data > value:
                break
            ptr_prev = ptr
            ptr = ptr.next_node

        new_node = Node(value, ptr)
        if ptr == self.head:
            self.head = new_node
        else:
            ptr_prev.next_node = new_node
