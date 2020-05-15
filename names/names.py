import time
from bst import BSTNode #use bst to search

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

#for name_1 in names_1:
 #   for name_2 in names_2:
  #      if name_1 == name_2:
   #         duplicates.append(name_1)

            ##runtime: 5.824483394622803 seconds


#use bst to search names list
#look over names, compare names in 1 to names in 2 
# can use contains methodd in BST for name. 
#append to duplicate
bst = BSTNode(names_1[0]) #start
for name_1 in names_1:
    bst.insert(name_1) #for every name in names 1, insert to tree

for name_2 in names_2: #for every name in 2: see if tree contains, if so add to duplicates[]
    if bst.contains(name_2):
        duplicates.append(name_2)

        ##BST runtime runtime: 0.07622146606445312ish seconds 
        # O(log n)?



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
