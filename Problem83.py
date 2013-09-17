matrix = [[int(n) for n in f.split(',')] for f in open('matrix2.txt').readlines()]

def problem_83(graph):
	nodes = []
	for i in xrange(0,len(graph)):
		for j in xrange(0,len(graph)):
			graph[i][j] = [graph[i][j], float('inf')]
	graph[0][0][1] = graph[0][0][0]
	length = len(graph)
	check = lambda node: graph[node[0]][node[1]][1]
	#list of Nodes
	nodes = [(i , j) for i in xrange(length) for j in xrange(length)]
	while len(nodes) > 0:
		node = min(nodes, key = check)
		nodes.remove(node)
		neighbours = []
		i, j = node[0], node[1]
		#Finding Neighbours
		bounds = lambda x: x < length and x >= 0
		for x in filter(bounds,(node[0] - 1, node[0] + 1)):
			neighbours.append((x , node[1]))
		for y in filter(bounds, (node[1] - 1, node[1] + 1)):
			neighbours.append((node[0], y))
		#for every neighbour not previously checked, see if its a smaller distance
		for neighbour in neighbours:
			if neighbour not in nodes: continue
			value = graph[node[0]][node[1]][1] + graph[neighbour[0]][neighbour[1]][0]
			if value < graph[neighbour[0]][neighbour[1]][1]:
				graph[neighbour[0]][neighbour[1]][1] = value
	return graph[-1][-1][1]

print problem_83(matrix)
