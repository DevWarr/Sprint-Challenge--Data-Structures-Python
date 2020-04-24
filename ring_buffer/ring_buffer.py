from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.oldest = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) == self.capacity:
            # If we're at capacity,
            # overwrite oldest node
            # and update self.oldest
            self.oldest.value = item

            if self.oldest == self.storage.tail:
                self.oldest = self.storage.head
            else:
                self.oldest = self.oldest.next
        else:
            # Add node in, increase capacity,
            # And set self.oldest if needed
            self.storage.add_to_tail(item)
            if len(self.storage) == 1:
                # If our capacity is 1, we just added
                # our first value, and that value
                # is the oldest
                self.oldest = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        curr_node = self.storage.head
        while curr_node is not None:
            list_buffer_contents.append(curr_node.value)
            curr_node = curr_node.next


        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    """
    A Ring Buffer, 
    with a Python list as the data structure for storage.

    This allows lists to be used peacefully, as we're never going 
    to append any extra data to this list. Once we reach the end
    of the list, we ring to the beginning, so the data
    we allocate in the beginning is the only data we need.
    """

    def __init__(self, capacity):
        self.storage = [None] * capacity
        self.current = 0

    def append(self, item):

        self.storage[self.current] = item
        self.current += 1

        if self.current == len(self.storage):
            # If we're at the end of our list, 
            # ring back around to the beginning
            self.current = 0

    def get(self):
        return [item for item in self.storage if item is not None]
