import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure


# # To test, highlight the whole block and un-comment
# # The actual comments have double '#' so you are free to 
# # uncomment the entire block - no need to just uncomment the code.
# print("Un comment this whole block, and I'm the only one that shows")



# # =============================================================
# #  MVP MVP MVP MVP MVP MVP MVP MVP MVP MVP MVP MVP MVP MVP MVP
# # Create Binary Search Tree with a middle letter of the alphabet.
# # This means most names will be more or less divided evenly.
# # (I didn't create a self balancing tree, 
# #     so this is my next best balancing act)

# bst = BinarySearchTree("M") 
# for name_1 in names_1:
#     bst.insert(name_1)
# for name_2 in names_2:
#     if bst.contains(name_2):
#         duplicates.append(name_2)
# # # =============================================================



# # =======================================
# # STRETCH STRETCH STRETCH STRETCH STRETCH
# # Stretch using a Set ↓↓ This guy is FAST
#
# name_set = set(names_1)
# for name_2 in names_2:
#     if name_2 in name_set:
#         duplicates.append(name_2)
# # =======================================



# # ====================================================
# #    STRETCH STRETCH STRETCH STRETCH STRETCH STRETCH
# # ****Stretch with no extra data structures****
# # Python cheating? Using the 'in' keyword, you can
# # Very quickly check if something exists inside another 
# # list. Final runtime about 1.2 seconds, no extra space
#
# for name_1 in names_1:
#     if name_1 in names_2:
#         duplicates.append(name_1)
# # ====================================================



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
