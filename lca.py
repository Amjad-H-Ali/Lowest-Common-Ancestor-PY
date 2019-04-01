from AtoT import array_to_tree


print("Lowest Common Ancestor!")


node = array_to_tree([3,11,5,2,6,17,4,7,9,13,21,14,8,19,1])


def LCA(root, node1, node2):
	# Return Null if no root
	if(not root):
		return None;

	if(root["value"] == node1 or root["value"] == node2):
		return root["value"]	

	left  = LCA(root["left"], node1, node2)

	right = LCA(root["right"], node1, node2)

	if(left and right):
		return root["value"]

	return left if left else right




print(LCA(node, 19, 21)) # 3

print(LCA(node, 2, 9))   # 2

print(LCA(node, 14, 8))  # 17

print(LCA(node, 6, 2))   # 11

print(LCA(node, 3, 5))   # 3 

print(LCA(node, 19, 1))  # 4