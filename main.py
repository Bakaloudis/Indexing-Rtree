import sys
import math

nodes_array = []
level_nodes = []

used_nodes = 0

inter_mbrs = 0
cont_mbrs = 0
ins_mbrs = 0


def intersect(mbr,qst):

	l1 = [mbr[0],mbr[3]]
	r1 = [mbr[1],mbr[2]]

	l2 = [qst[0],qst[3]]
	r2 = [qst[1],qst[2]]

	if(l1[0]>r2[0] or l2[0]>r1[0]):
		return ('false')

	if(l1[1]<r2[1] or l2[1]<r1[1]):
		return ('false')

	return ('true')


def contains(mbr,qst):

	l1 = [qst[0],qst[3]]
	r1 = [qst[1],qst[2]]

	l2 = [mbr[0],mbr[3]]
	r2 = [mbr[1],mbr[2]]

	if (l1[0]>=l2[0] and r1[0]<=r2[0]):
		if (l1[1]<=l2[1] and r1[1]>= r2[1]):
			return ('true')
	return ('false')


def inside(mbr,qst):

	l1 = [mbr[0],mbr[3]]
	r1 = [mbr[1],mbr[2]]

	l2 = [qst[0],qst[3]]
	r2 = [qst[1],qst[2]]

	if (l1[0]>=l2[0] and r1[0]<=r2[0]):
		if (l1[1]<=l2[1] and r1[1]>= r2[1]):
			return ('true')
	return ('false')



def range_query_inside(qst_mbr,node):

	global nodes_array
	global level_nodes

	global used_nodes
	global ins_mbrs

	used_nodes+=1

	counter=0
	for value in nodes_array:
		counter+=1
		if value == node:	
			break

	if(counter>level_nodes[0]):		# the node is not a leaf node
		for mid_node in node:

			mid_node_id=mid_node[0]
			mid_node_cor=mid_node[1:]

			if(intersect(mid_node_cor,qst_mbr) == 'true'):
				node = nodes_array[int(mid_node_id)]
				range_query_inside(qst_mbr,node)

	else:							# the node is a leaf node

		for mbr in node:
			mbr_id=mbr[0]
			mbr_cor=mbr[1:]

			if(inside(mbr_cor,qst_mbr) == 'true'):
				ins_mbrs+=1


def range_query_contain(qst_mbr,node):

	global nodes_array
	global level_nodes

	global used_nodes
	global cont_mbrs

	used_nodes+=1

	counter=0
	for value in nodes_array:
		counter+=1
		if value == node:	
			break

	if(counter>level_nodes[0]):		# the node is not a leaf node
		for mid_node in node:

			mid_node_id=mid_node[0]
			mid_node_cor=mid_node[1:]

			if(intersect(mid_node_cor,qst_mbr) == 'true'):
				node = nodes_array[int(mid_node_id)]
				range_query_contain(qst_mbr,node)

	else:							# the node is a leaf node

		for mbr in node:
			mbr_id=mbr[0]
			mbr_cor=mbr[1:]

			if(contains(mbr_cor,qst_mbr) == 'true'):
				cont_mbrs+=1


def range_query(qst_mbr,node):

	global nodes_array
	global level_nodes

	global used_nodes
	global inter_mbrs

	used_nodes+=1

	counter=0
	for value in nodes_array:
		counter+=1
		if value == node:	
			break

	if(counter>level_nodes[0]):		# the node is not a leaf node
		for mid_node in node:

			mid_node_id=mid_node[0]
			mid_node_cor=mid_node[1:]

			if(intersect(mid_node_cor,qst_mbr) == 'true'):
				node = nodes_array[int(mid_node_id)]
				range_query(qst_mbr,node)

	else:							# the node is a leaf node

		for mbr in node:
			mbr_id=mbr[0]
			mbr_cor=mbr[1:]

			if(intersect(mbr_cor,qst_mbr) == 'true'):
				inter_mbrs+=1
				



def create_nodes(nodes_array,prev_nodes):


	N = 28 # number of children each node can have

	node_x_low = []
	node_x_high = []
	node_y_low = []
	node_y_high = []

	final_list = []
	dummy = []

	father_nodes = 0

	nodes_counter = 0
	length = len(nodes_array) - 1

	temp_counter = 0

	for value in nodes_array:
		temp_counter+=1
		if temp_counter > (length + 1)  - prev_nodes: # kanw skip ta nodes tou prohgoumenoy epipedou
			nodes_counter+=1
			if nodes_counter<N: 		# elegxw ta child nodes ana N
				if value == nodes_array[length] : # elegxw an eftasa sto teleutaio child node
					MBRs=value
					temp = 0
					for val in MBRs: # elegxw ka8e MBR tou child node 3exwrista
						temp+=1				 
						node_x_low.append(val[1])
						node_x_high.append(val[2])
						node_y_low.append(val[3])
						node_y_high.append(val[4])

					node_x_low.sort() 
					node_x_high.sort()
					node_y_low.sort() 
					node_y_high.sort()

					dummy.append(str(temp_counter-1))
					dummy.append(node_x_low[0])
					dummy.append(node_x_high[temp-1])
					dummy.append(node_y_low[0])
					dummy.append(node_y_high[temp-1])

					final_list.append(dummy) 		# dhmiourgw stadiaka ton father node
					father_nodes +=1
					nodes_array.append(final_list)
					break					# eftasa sto telos twn children nodes

				MBRs=value
				temp=0
				for val in MBRs:
					temp+=1 				# elegxw ka8e MBR tou child node 3exwrista 
					node_x_low.append(val[1])
					node_x_high.append(val[2])
					node_y_low.append(val[3])
					node_y_high.append(val[4])

				node_x_low.sort() 
				node_x_high.sort()
				node_y_low.sort() 
				node_y_high.sort()

				dummy.append(str(temp_counter-1))
				dummy.append(node_x_low[0])
				dummy.append(node_x_high[temp-1])
				dummy.append(node_y_low[0])
				dummy.append(node_y_high[temp-1])

				final_list.append(dummy) 		# dhmiourgw stadiaka ton father node 

				dummy = []
				node_x_low = []
				node_x_high = []
				node_y_low = []
				node_y_high = []
			else:							# bainw sthn else an brw to teleutaio child node poy xwraei ston father 
				MBRs=value
				temp=0
				for val in MBRs: 				# elegxw ka8e MBR tou child node 3exwrista 
					temp+=1
					node_x_low.append(val[1])
					node_x_high.append(val[2])
					node_y_low.append(val[3])
					node_y_high.append(val[4])

				node_x_low.sort() 
				node_x_high.sort()
				node_y_low.sort() 
				node_y_high.sort()

				dummy.append(str(temp_counter-1))
				dummy.append(node_x_low[0])
				dummy.append(node_x_high[temp-1])
				dummy.append(node_y_low[0])
				dummy.append(node_y_high[temp-1])

				final_list.append(dummy) 		# dhmiourgw stadiaka ton father node
				father_nodes +=1
				nodes_array.append(final_list)

				dummy = []
				node_x_low = []
				node_x_high = []
				node_y_low = []
				node_y_high = []


				final_list = []
				nodes_counter=0

	return nodes_array , father_nodes


def main():

	global nodes_array
	global level_nodes

	global used_nodes
	global inter_mbrs
	global cont_mbrs
	global ins_mbrs

	file1 = open(sys.argv[1], 'r') 
	Lines = file1.readlines() 

	output_file = open('rtree.txt' , 'w')

	N = 28 # number of children each node can have
	R = 0 # number of MBRs

	nodes_dict = {}

	mbrs = []

	for line in Lines: 	
		temp_lister = []

		line = '\t'.join(line.split())
		temp_list = line.split("\t")

		temp_lister.append(temp_list[0])
		temp_lister.append(float(temp_list[1]))
		temp_lister.append(float(temp_list[2]))
		temp_lister.append(float(temp_list[3]))
		temp_lister.append(float(temp_list[4]))

		mbrs.append(temp_lister)


	R = len(mbrs)

	mbrs.sort(key=lambda x: float(x[1]))  # sorting by x-low

	P = math.ceil(R/N)
	S = math.ceil(math.sqrt(P))

	counter = 0
	dict_index = -1

	temp_mbrs = []

	for i in range (0,R):  				# i create the leaf nodes
		counter+=1
		if(counter < (S*N) ):			# spliting the mbrs list by (S * N)
			temp_mbrs.append(mbrs[i])
			if i == R-1: 				# in case we check the last MBR
				temp_mbrs.sort(key=lambda x: float(x[3])) # sorting by y-low
				dummy = 0
				final_mbrs = []
				for value in temp_mbrs:			# creating the leaf node every N mbrs
					dummy+=1
					if dummy<N:
						final_mbrs.append(value)
						if value == temp_mbrs[len(temp_mbrs)-1]: 	# i check the EOF
							nodes_array.append(final_mbrs)
							break
					else:
						final_mbrs.append(value)
						nodes_array.append(final_mbrs)
						dummy = 0
						final_mbrs = []
		else:
			temp_mbrs.append(mbrs[i])
			temp_mbrs.sort(key=lambda x: float(x[3])) # sorting by y-low after the split

			dummy = 0
			final_mbrs = []
			for value in temp_mbrs:
				dummy+=1
				if dummy<N:							 # creating the leaf node every N mbrs
					final_mbrs.append(value)
				else:
					final_mbrs.append(value)
					nodes_array.append(final_mbrs)
					dummy = 0
					final_mbrs = []

			temp_mbrs= []
			counter = 0

	#-----------------------------------------------------------#

	temp = 0
	for value in nodes_array:  
		temp+=1
	level_nodes.append(temp)

	father_nodes = level_nodes[0]

	while father_nodes > N:   									# i create the mid level nodes
		result = create_nodes(nodes_array,father_nodes)
		nodes_array = result[0]
		father_nodes = result[1]
		level_nodes.append(father_nodes)
  	
	result = create_nodes(nodes_array,father_nodes)				# i create the root node
	nodes_array = result[0]
	father_nodes = result[1]
	level_nodes.append(father_nodes)

	tree_height = 0
	for i in range(0,len(level_nodes)):
		tree_height+=1

	root_node_id = len(nodes_array)
	output_file.write(str(root_node_id-1) + '\n')	# writting the node-id of the root

	output_file.write(str(tree_height) + '\n')		# writting the height of the tree

	temp = -1
	for value in nodes_array:			# writting all the nodes with the needed information
		temp+=1
		string = ''
		string+=str(temp) + ', '
		string+=str(len(value)) + ', '
		string+=str(value)
		output_file.write(string + '\n')

	print('\n')
	print('#---------------------------PRWTO MEROS----------------------------#')	

	print('\n')
	print('tree height: ' + str(tree_height) )
	print('\n')

	for i in range(len(level_nodes)-1,-1,-1):
		print('level ' + str(i) + ': ' + 'number of nodes --> ' + str(level_nodes[i]))
	print('\n')

	prev=0
	area_list = []
	average_area_list = []
	for value in level_nodes:
		for i in range(prev,value+prev):
			for mbr in nodes_array[i]:
				mbr_cor=mbr[1:]
				mbr_height=mbr_cor[3] - mbr_cor[2]		# height of MBR
				mbr_width=mbr_cor[1] - mbr_cor[0]		# width of MBR
				mbr_area = mbr_width * mbr_height
				area_list.append(mbr_area)

		average_area = sum(area_list)/len(area_list)
		average_area_list.append(average_area)
		prev+=value
		area_list = []

	for i in range(len(average_area_list)-1,-1,-1):
		print('level ' + str(i) + ': ' + 'average area of MBRs --> ' + str(average_area_list[i]))
	print('\n')


	#----------------------------------------------------------------------------------#


	#----------------------------------DEUTERO MEROS-----------------------------------#


	#----------------------------------------------------------------------------------#

	print('#---------------------------DEUTERO MEROS----------------------------#\n')


	file2 = open('query_rectangles.txt', 'r') 
	Lines = file2.readlines()
	query = [] 
	for line in Lines: 	
		temp_lister = []

		line = '\t'.join(line.split())
		temp_list = line.split("\t")

		temp_lister.append(temp_list[0])
		temp_lister.append(float(temp_list[1]))
		temp_lister.append(float(temp_list[2]))
		temp_lister.append(float(temp_list[3]))
		temp_lister.append(float(temp_list[4]))

		query.append(temp_lister)

	for value in query:

		range_query(value[1:],nodes_array[len(nodes_array)-1]) # ksekinaw dinontas to root node
		print('query-id: ' + value[0])
		print('nodes that have been accesed : ' + str(used_nodes))
		print('MBRs that intersected with the given query: ' + str(inter_mbrs))

		used_nodes = 0
		range_query_inside(value[1:],nodes_array[len(nodes_array)-1]) # ksekinaw dinontas to root node
		print('MBRs that are inside the given query: ' + str(ins_mbrs))

		used_nodes = 0
		range_query_contain(value[1:],nodes_array[len(nodes_array)-1]) # ksekinaw dinontas to root node
		print('MBRs that contained the given query: ' + str(cont_mbrs) + '\n')

		used_nodes = 0
		inter_mbrs = 0
		ins_mbrs = 0
		cont_mbrs = 0
		

	output_file.close
	file1.close
	file2.close



main()