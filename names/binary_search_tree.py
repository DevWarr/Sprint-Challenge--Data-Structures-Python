
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        curr_node = self
        while True:
            # Keep looping until we place our value in the tree

            if value < curr_node.value:
                # If our value is less,
                # it needs to go to the left side of the tree
                if curr_node.left is None:
                    # If there's no node, create one and break
                    curr_node.left = BinarySearchTree(value)
                    break
                else:
                    # If there is a node, repeat the loop!
                    curr_node = curr_node.left
                    continue
            else:
                # If our value is equal to or greater than,
                # it needs to go to the right side of the tree
                if curr_node.right is None:
                    # If there's no node, create one and break
                    curr_node.right = BinarySearchTree(value)
                    break
                else:
                    # If there is a node, repeat the loop!
                    curr_node = curr_node.right
                    continue


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        curr_node = self
        while curr_node is not None:
            # We'll leave our loop if we end up on a None
            #     node, and return False
            if target == curr_node.value:
                return True
            elif target < curr_node.value:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right

        # Ending the while loop naturally?
        # that means we didn't find a match
        return False


    # Return the maximum value found in the tree
    def get_max(self):
        curr_node = self
        max_val = curr_node.value
        while curr_node.right is not None:
            curr_node = curr_node.right
            max_val = curr_node.value
        return max_val
