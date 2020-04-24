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
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
