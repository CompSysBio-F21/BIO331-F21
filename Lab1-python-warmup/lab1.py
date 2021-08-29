## Bio331 Fall 2021
## Lab1: Python Warm Up

def main():
	"""
	Main function. There are no inputs
	(nodes and matrix are specified within this function)
	"""

	## List of node names
	nodes = ['A','B','C','D','E','F']
	## Adjacency matrix (assume this represents an undirected graph & has same order as nodes)
	adj_mat = [[0,1,0,1,0,1],[1,0,0,0,1,1],[0,0,0,1,0,0],[1,0,1,0,0,0],[0,1,0,0,1,1],[1,1,0,0,1,0]]

	## function calls
	print('\n2. Working with Adjacency Matrices:')
	print_mat(nodes,adj_mat)

	print('\n3. From an Adjacency Matrix to an Adjacency List')
	adj_list = mat_to_list(nodes,adj_mat)
	print_list(adj_list)

	print('\n4. Count the number of nodes and edges, two ways.')
	n,m = count_from_adj_mat(adj_mat)
	print('{} nodes and {} edges from adjacency matrix'.format(n,m))

	n,m = count_from_adj_list(adj_list)
	print('{} nodes and {} edges from adjacency list'.format(n,m))

	print('\nDone!')
	return # done with main function

def print_mat(nodes,adj_mat):
	"""
	Prints the adjacency matrix
	Inputs: nodes (list of strings) and adj_mat (list of lists)
	Returns: nothing
	"""

	print("FILL IN") # comment this line out as you complete the function

	return # returns nothing

def mat_to_list(nodes,adj_mat):
	"""
	Converts the adjacency matrix to an adjacency list
	Inputs: nodes (list of strings) and adj_mat (list of lists)
	Returns: adjacency list (dictionary of (node,neighbor list) pairs).
	"""

	print("FILL IN") # comment this line out as you complete the function

	return {} # replace this with the variable to return

def print_list(adj_list):
	"""
	Prints the adjacency list
	Inputs: adj_list (dictionary of (node,list) pairs)
	Returns: nothing
	"""

	print("FILL IN") # comment this line out as you complete the function

	return # returns nothing

def count_from_adj_mat(adj_mat):
	"""
	Counts the number of edges from the adjacency matrix
	Inputs: adj_mat (list of lists)
	Returns: the number of nodes (int) and the number of edges (int)
	"""

	print("FILL IN") # comment this line out as you complete the function

	return -1,-1

def count_from_adj_list(adj_list):
	"""
	Counts the number of edges from the adjacency list
	Inputs: adj_list (dictionary of (node,list) pairs)
	Returns: the number of nodes (int) and the number of edges (int)
	"""

	print("FILL IN") # comment this line out as you complete the function

	return -1,-1

"""
 Leave this is at the bottom of the file. Once all functions are loaded, then
 main() is called UNLESS you are importing this file into another script.
 See https://docs.python.org/3/library/__main__.html
"""
if __name__ == '__main__':
	main()
