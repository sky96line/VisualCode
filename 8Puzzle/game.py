from __future__ import print_function
import sys
import os
import time

def display(state):
	print()
	for i in range(9):
		if(i % 3 is 0):
			print()
		print(state[i], end=" ")
		

def move_up(state):
	new_state = state[:]
	index = new_state.index(0)
	if index not in [0, 3, 6]:
		temp = new_state[index - 1]
		new_state[index - 1] = new_state[index]
		new_state[index] = temp
		if new_state in close:
			return None
		return new_state
	else:
		return None


def move_down(state):
	new_state = state[:]
	index = new_state.index(0)
	if index not in [2, 5, 8]:
		temp = new_state[index + 1]
		new_state[index + 1] = new_state[index]
		new_state[index] = temp
		if new_state in close:
			return None
		return new_state
	else:
		return None


def move_left(state):
	new_state = state[:]
	index = new_state.index(0)
	if index not in [0, 1, 2]:
		temp = new_state[index - 3]
		new_state[index - 3] = new_state[index]
		new_state[index] = temp
		if new_state in close:
			return None
		return new_state
	else:
		return None


def move_right(state):
	new_state = state[:]
	index = new_state.index(0)
	if index not in [6, 7, 8]:
		temp = new_state[index + 3]
		new_state[index + 3] = new_state[index]
		new_state[index] = temp
		if new_state in close:
			return None
		return new_state
	else:
		return None

class Node:
	def __init__(self, state, parent, operator, depth, cost):
		self.state = state
		self.parent = parent
		self.operator = operator
		self.depth = depth
		self.cost = cost

def create_node( state, parent, operator, depth, cost ):
	return Node( state, parent, operator, depth, cost )

def expand_node( node, nodes ):
	"""Returns a list of expanded nodes"""
	expanded_nodes = []
	expanded_nodes.append( create_node( move_up( node.state ), node, "r", node.depth + 1, 0 ) )
	expanded_nodes.append( create_node( move_down( node.state ), node, "l", node.depth + 1, 0 ) )
	expanded_nodes.append( create_node( move_left( node.state ), node, "d", node.depth + 1, 0 ) )
	expanded_nodes.append( create_node( move_right( node.state), node, "u", node.depth + 1, 0 ) )
	# Filter the list and remove the nodes that are impossible (move function returned None)
	expanded_nodes = [node for node in expanded_nodes if node.state != None] #list comprehension!
	#print(len(expanded_nodes))
	return expanded_nodes


def bfs(start, goal):
	speed = 0
	print('Working...')
	nodes = []
	nodes.append(create_node(start, None, None, 0, 0))
	t = time.time()
	while True:
		if len(nodes) == 0:
			return None
		node = nodes.pop(0)
		speed += 1
		#close.append(node.state)
		
		if speed > 10000:
			speed = 0
			tt = time.time() - t
			print(tt)
			t = tt
			display(node.state)
		#display(node.state)
		#time.sleep(3)
		
		if node.state == goal:
			moves = []
			temp = node
			while True:
				moves.insert(0, temp.operator)
				if temp.depth == 1:
					break
				temp = temp.parent
			return moves
		nodes.extend(expand_node(node, nodes))

def disp(arr):
	for k in arr:
		print()
		display(k)

goal = [1,2,3,
				8,0,4,
				7,6,5]
close = []
def main():
	start = [1,2,3,
					 4,5,6,
					 7,8,0]
	result = bfs(start, goal)
	if result == None:
	  print("No solution found")
		
	elif result == [None]:
		print("Start node was the goal!")
	else:
		print (result)
		print (len(result), " moves")
	#disp(close)

if __name__ == "__main__":
	main()
