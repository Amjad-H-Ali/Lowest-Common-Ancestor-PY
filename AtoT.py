
# print("Array To Tree!")

# Function takes in an array and returns a tree

def array_to_tree(array, index=0):

	# If index out of range (exit code for reccursion)
	if index >= len(array):
		return None

	# Define and initialize left and right children nodes
	left = (index * 2) + 1

	right = left + 1	

	# Return tree using reccursion
	return {

		"value" : array[index],

		"left"  : array_to_tree(array, left),

		"right" : array_to_tree(array, right)
	}

# arr = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# print(array_to_tree(arr))	

# print(array_to_tree(arr)["left"]["left"]["left"]["left"]["value"]) # 0