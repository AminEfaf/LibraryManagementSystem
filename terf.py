import os
from io import StringIO
import sys


class Node:
	
	def __init__(self, key):
		
		self.key = key
		self.child = []

# Utility function to create a new tree node
def newNode(key):
	temp = Node(key)
	return temp
	
# Prints the n-ary tree level wise
def LevelOrderTraversal(root):

	q = [] # Create a queue

	q.append(root)  # Enqueue root
    
	while (len(q) != 0):
	
		n = len(q) 

		# If this node has children
		while (n > 0):
		
			# Dequeue an item from queue and print it
			p = q[0]
			q.pop(0)
			print(p.key, end=' ')

			# Enqueue all children of the dequeued item
			for i in range(len(p.child)):
			
				q.append(p.child[i]) 
			n -= 1

		print() # Print new line between two levels

# inorder traversal
def inorder(name): 
	for i in nodes:
		if Dict[i] == name:
			return i

  
# To heapify subtree rooted at index i. 
def heapify(arr, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest) 
  
# The main function to sort an array of given size 
def heapSort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0) 
  


# Driver program
if __name__=='__main__':
	# Clearing the Screen
	os.system('clear')

	nodes = []
	lst = []
	Dict = {}
	Books = {}

	# Making a sample library
	root = newNode("root") 
	nodes.append(root)
	Dict[root] = "root"
	Daneshgahi = newNode("Daneshgahi")
	(root.child).append(Daneshgahi)
	nodes.append(Daneshgahi)
	Dict[Daneshgahi] = "Daneshgahi"
	Omoumi = newNode("Omoumi")
	(root.child).append(Omoumi) 
	nodes.append(Omoumi)
	Dict[Omoumi] = "Omoumi"
	Fani_mohandesi = newNode("Fani mohandesi")
	(root.child[0].child).append(Fani_mohandesi) 
	nodes.append(Fani_mohandesi)
	Dict[Fani_mohandesi] = "Fani_mohandesi"
	Oloum_ensani = newNode("Oloum ensani")
	(root.child[0].child).append(Oloum_ensani) 
	nodes.append(Oloum_ensani)
	Dict[Oloum_ensani] = "Oloum_ensani"
	Oloum_paye = newNode("Oloum paye")
	(root.child[0].child).append(Oloum_paye) 
	nodes.append(Oloum_paye)
	Dict[Oloum_paye] = "Oloum_paye"
	Bargh = newNode("Bargh")
	(root.child[0].child[0].child).append(Bargh) 
	nodes.append(Bargh)
	Dict[Bargh] = "Bargh"                                
	Computer = newNode("Computer")
	(root.child[0].child[0].child).append(Computer) 
	nodes.append(Computer)
	Dict[Computer] = "Computer"
	Sakhteman_haye_dadeBook = "Sakhteman haye dade-Mohammad Ghodsi-14$".split("-")
	Sakhteman_haye_dade = newNode(Sakhteman_haye_dadeBook[0])
	(root.child[0].child[0].child[1].child).append(Sakhteman_haye_dade)
	nodes.append(Sakhteman_haye_dade) 
	Dict[Sakhteman_haye_dade] = "Sakhteman_haye_dade"
	Books[Sakhteman_haye_dadeBook[0]] = "Writer:"+Sakhteman_haye_dadeBook[1]+" - Price:"+Sakhteman_haye_dadeBook[2]
	System_amelBook = "System amel-Kambiz Sedaghat-10$".split("-")
	System_amel = newNode(System_amelBook[0])
	(root.child[0].child[0].child[1].child).append(System_amel) 
	nodes.append(System_amel)
	Dict[System_amel] = "System_amel"
	Books[System_amelBook[0]] = "Writer:"+System_amelBook[1]+" - Price:"+System_amelBook[2]
	Zaban_assemblyBook = "Zaban assembly-Allen Chapman-15$".split("-")
	Zaban_assembly = newNode(Zaban_assemblyBook[0])
	(root.child[0].child[0].child[1].child).append(Zaban_assembly) 
	nodes.append(Zaban_assembly)
	Dict[Zaban_assembly] = "Zaban_assembly"
	Books[Zaban_assemblyBook[0]] = "Writer:"+Zaban_assemblyBook[1]+" - Price:"+Zaban_assemblyBook[2]
	Jonathan_va_morgh_daryaiBook = "Jonathan va morgh daryai-Richard Bach-18$".split("-")
	Jonathan_va_morgh_daryai = newNode(Jonathan_va_morgh_daryaiBook[0])
	(root.child[1].child).append(Jonathan_va_morgh_daryai) 
	nodes.append(Jonathan_va_morgh_daryai)
	Dict[Jonathan_va_morgh_daryai] = "Jonathan_va_morgh_daryai"
	Books[Jonathan_va_morgh_daryaiBook[0]] = "Writer:"+Jonathan_va_morgh_daryaiBook[1]+" - Price:"+Jonathan_va_morgh_daryaiBook[2]
	Fantasy = newNode("Fantasy")
	(root.child[1].child).append(Fantasy) 
	nodes.append(Fantasy)
	Dict[Fantasy] = "Fantasy"
	Arbab_halghe_haBook =  "Arbab halghe ha-J. R. R. Tolkien-18$".split("-")
	Arbab_halghe_ha = newNode(Arbab_halghe_haBook[0])
	(root.child[1].child[1].child).append(Arbab_halghe_ha) 
	nodes.append(Arbab_halghe_ha)
	Dict[Arbab_halghe_ha] = "Arbab_halghe_ha"
	Books[Arbab_halghe_haBook[0]] = "Writer:"+Arbab_halghe_haBook[1]+" - Price:"+Arbab_halghe_haBook[2]


	while True:
		print()
		x = input("Input:")

		# Clearing the Screen
		os.system('clear')

		if x[0:12] == "add category": 
			# Making a node with given information
			globals()[x[14:x.find(">")].replace(" ", "_")] = newNode(x[14:x.find(">")])

			# Adding chid node to father node
			(root.child).append(globals()[x[14:x.find(">")].replace(" ", "_")]) 

			nodes.append(globals()[x[14:x.find(">")].replace(" ", "_")])
			Dict[globals()[x[14:x.find(">")].replace(" ", "_")]] = x[14:x.find(">")].replace(" ", "_")

			print("Done!")
		elif x[0:15] == "add subcategory": 
			# Finding father node
			foundedCategory = inorder(x[x.find("to")+4:len(x)-1].replace(" ", "_"))

			# Making a node with given information
			globals()[x[17:x.find(">")].replace(" ", "_")] = newNode(x[17:x.find(">")])

			# Adding chid node to father node
			(foundedCategory.child).append(globals()[x[17:x.find(">")].replace(" ", "_")])

			nodes.append(globals()[x[17:x.find(">")].replace(" ", "_")])
			Dict[globals()[x[17:x.find(">")].replace(" ", "_")]] = x[17:x.find(">")].replace(" ", "_")
			
			print("Done!")
		elif x[0:8] == "add book":
			a = x[10:x.find(">")].split("-")
			# Making a node with given information
			globals()[a[0].replace(" ", "_")] = newNode(a[0])

			# Finding father node
			foundedCategory = inorder(x[x.find("to")+4:len(x)-1].replace(" ", "_"))

			# Adding chid node to father node
			(foundedCategory.child).append(globals()[a[0].replace(" ", "_")])

			nodes.append(globals()[a[0].replace(" ", "_")])
			Dict[globals()[a[0].replace(" ", "_")]] = a[0].replace(" ", "_")
			Books[a[0]] = "Writer:"+a[1]+" - Price:"+a[2]
			
			print("Done!")
		elif x[0:11] == "remove book":	
			# Finding father node	
			foundedCategory = inorder(x[x.find("from")+6:len(x)-1].replace(" ", "_"))
			# Finding child node	
			foundedBook = inorder(x[13:x.find(">")].replace(" ", "_"))
			# Removing chid node from father node
			(foundedCategory.child).remove(foundedBook)
			nodes.remove(foundedBook)
			del Books[x[13:x.find(">")]]

			print("Done!")
		elif x[0:15] == "remove category":
			# If the given category was root! 
			if x[17:x.find(">")].replace(" ", "_") == "root":
				(root.child).clear()
				nodes.remove(root)

				print("Done!")
			else:
				childNode = inorder(x[17:x.find(">")].replace(" ", "_"))

				# Storing the tree elements in the variable
				buffer = StringIO()
				sys.stdout = buffer
				LevelOrderTraversal(childNode)
				finalTree = buffer.getvalue()
				sys.stdout = sys.__stdout__

				# Finding the father node and removing the chid node
				for fatherNode in nodes:
					for k in range(len(fatherNode.child)):
						if fatherNode.child[k] == childNode:
							(childNode.child).clear()
							(fatherNode.child).remove(fatherNode.child[k])
							nodes.remove(childNode)
							break

				# Removing the books of the category 
				for i in list(Books):
					if i in finalTree:
						del Books[i]	

				print("Done!")			

		elif x[0:6] == "search":
			print(x[x.find("<")+1:x.find(">")] + " : " +Books[x[x.find("<")+1:x.find(">")]])
		elif x == "list books":
			[print(key,':',value) for key, value in Books.items()]
		elif x[0:15] == "list books from":
			foundedCategory = inorder(x[17:x.find(">")])

			# Storing the tree elements in the variable
			buffer = StringIO()
			sys.stdout = buffer
			LevelOrderTraversal(foundedCategory)
			finalTree = buffer.getvalue()
			sys.stdout = sys.__stdout__

			for i in Books.keys():
				if i in finalTree:
					print(i + ": " + Books[i])

		elif x[0:5] == "order":
			if x[7:x.find(">")] in Books.keys():
				price = int(Books[x[7:x.find(">")]][Books[x[7:x.find(">")]].find("Price:")+6:Books[x[7:x.find(">")]].find("$")])

				# Storing books information in order list
				lst.append([price, x[7:x.find(">")]])

				lst2 = []
				for i in range(len(lst)):
					lst2.append(lst[i][0])

				print("Done!")
			else:
				print("There is no such a book!")

		elif x == "list orders":
			# Adding prices to the heap and sorting them
			heapSort(lst2) 


			# Printing the final order list
			for i in list(dict.fromkeys(lst2[::-1])):
				for j in lst:
					if i == j[0]:
						print(j[1])
		
		elif x == "show":
			LevelOrderTraversal(root)

		elif x == "exit":
			quit()
			


