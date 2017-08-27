import sys
import numpy as np


fname = sys.argv[1]
fp = open(fname, 'r')
noOfNodes = int(fp.readline())
graph={}
edges=set()
# temp = -1
for line in fp:
	# print (line)
	l1 = line.strip().split(":")
	node = int(l1[0])
	l1[1] = l1[1].split(",")
	adjList = list(map(int, l1[1]))
	# print (l1)
	graph[node] = adjList
	# temp = node
	# edges.add(tuple(map(pair, adjList)))
	for j in adjList:
		if( ((node,j) not in edges) and ((j, node) not in edges) ):
			edges.add((node, j))

	# for i in range(len(adjList)):
	# 	print(edges)


print (graph.keys())
print(edges)
initialState = set()
currentState = set()
initialState.add(next(iter(edges)))
# print (initialState)
currentState.add(next(iter(initialState))) 
print (currentState)
print (np.power(len(edges), 2)* noOfNodes)
c=3
for i in range(c*np.power(len(edges), 2)* noOfNodes):
	U = np.random.uniform(0,1)
	print ("iteration :", i)
	if(U >= 0.5):
		# print("iteration:", i)
		(u,v) = tuple(edges)[np.random.randint(len(edges))]
		print(u,v)
		countOf_u_forCase1_3 = 0
		countOf_v_forCase1_3 = 0
		case2 = 0  
		flagv = 0
		flagu = 0
		for (udash, vdash) in currentState:
			if((u == udash) or (u == vdash)):
				countOf_u_forCase1_3 = 1
				if(u == udash):
					matchedVertexFor_u = vdash
				else:
					matchedVertexFor_u = udash
					flagu = 1
			if(v == udash or v == vdash):
				countOf_v_forCase1_3 = 1
				if(v == udash):
					matchedVertexFor_v = vdash
				else:
					matchedVertexFor_v = udash
					flagv = 1
			if( (u == udash and v == vdash) or (u == vdash and v == udash) ):
				case2 = 1

		nextState = currentState
		if(countOf_u_forCase1_3 == 0 and countOf_v_forCase1_3 == 0):
		    # nextState = currentState.add((u,v))
		    nextState.add((u,v))
		elif(countOf_u_forCase1_3 == 0 and countOf_v_forCase1_3 == 1):
		    if(flagv == 1):
		        # currentState.remove((matchedVertexFor_v, v))
		        nextState.remove((matchedVertexFor_v, v))
		    else:
		        # currentState.remove((v, matchedVertexFor_v))
		        nextState.remove((v, matchedVertexFor_v))
		    # nextState = currentState.add((u,v))
		    nextState.add((u,v))
		elif(countOf_u_forCase1_3 == 1 and countOf_v_forCase1_3 == 0):
		    if(flagu == 1):
		        # currentState.remove((matchedVertexFor_u, u))
		        nextState.remove((matchedVertexFor_u, u))
		    else:
		        # currentState.remove((u, matchedVertexFor_u))
		        nextState.remove((u, matchedVertexFor_u))
		    # nextState = currentState.add((u,v))
		    nextState.add((u,v))
		elif(case2 == 1):
		    # nextState = currentState.remove((u,v))
		    nextState.remove((u,v))
		else:
		    nextState = currentState


		currentState = nextState

	print(currentState)


finalState = currentState
print("finalState is:" , finalState)

