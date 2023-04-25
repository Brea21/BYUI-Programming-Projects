# Import the math module so that we can call the math.ceil function.
import math

# Get two numbers from the user.
num_items = int(input(f"Enter the number of the items: ")) 
items_per_box = int(input(f"Enter the number of items per box: ")) 

# Compute the number of boxes by dividing
# and then calling the math.ceil function.
num_boxes = math.ceil(num_items / items_per_box)

# Display a blank line.
print()

# Display the results for the user to see.
print(f"For {num_items} items, packing {items_per_box} " f"items in each box, you will need {num_boxes} boxes.")
