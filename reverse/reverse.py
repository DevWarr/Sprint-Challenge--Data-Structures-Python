class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we
        # traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our
            # target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def __reverse_list(self, node, prev):

        # You must use recursion for this solution
        if node is None:
            return
        if node.next_node is None:
            self.head = node

        self.__reverse_list(node.next_node, node)
        node.next_node = prev
        
    def reverse_list(self, node=None, prev=None):
        """
        The public reverse_list method.

        No matter what's passed into this function,
        it will always rever the linked list starting at the 
        head.

        If you had a list like:
          0 → 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10

        If you called the above function like
          __reverse_list([node with value of 5])

        You would end up with a linked list like:
          0 → 1 → 2 → 3 → 4 → 5 ← 6 ← 7 ← 8 ← 9 ← 10
        Where is the head in this case . . ?
        
        This newer function ensures that we always
        start reversing at the head of the list.
        """
        self.__reverse_list(self.head, None)