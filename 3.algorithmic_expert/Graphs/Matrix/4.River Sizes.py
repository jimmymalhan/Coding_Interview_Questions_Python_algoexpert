# Problem Name: River Sizes

# Problem Description:
# You are given a two-dimensional array (matrix) of potentially unequal height and width containing only 0s and 1s. Each 0 represents land, and each 1 represents part of a river. A river consists of any number of 1s that are either horizontally or vertically adjacent (but not diagonally adjacent). The number of adjacent 1s forming a river determine its size. Write a function that returns an array of the sizes of all rivers represented in the input matrix. Note that these sizes do not need to be in any particular order. 

####################################
# Sample Input:
# matrix = [
#     [1, 0, 0, 1, 0],
#     [1, 0, 1, 0, 0],
#     [0, 0, 1, 0, 1],
#     [1, 0, 1, 0, 1],
#     [1, 0, 1, 1, 0],
# ]

# Sample Output:
# [1, 2, 2, 2, 5]

## The rivers can be clearly seen below.
# [
#     [1, , , 1,  ],
#     [1, ,1,  ,  ],
#     [ , ,1,  , 1],
#     [1, ,1,  , 1],
#     [1, ,1, 1,  ],
# ]

# Solution explanation:
# 1: 1 # there is only one 1
# 2: 2 # there are two 1s in a row
# 3: 2 # there are two 1s in a row
# 4: 2 # there are two 1s in a row
# 5: 5 # there are five 1s in a L shaped row

####################################
"""
stacks = depth first search

Explain the Solution:
1. Return the sizes of the rivers horizontally and vertically adjacent 1s in as traversing the matrix. Treat matrix as a graph where each element is a node with upto 4 neighbors nodes(left, right, top, bottom) and traverse the graph using DFS.
2. While traversing the matrix, anytime you encounter a 1, traverse entire river that this `1` is part of (keep track of the size of the river) by node's neighboring nodes and their own neighboring nodes as long as they are 1s. if you encounter a 0, mark it as visited and continue.
3. In order to prevent mistakenly calculating the size of the river multiple times, use auxiliary data structure "queue" to perform computation on unvisited nodes only.
O(wh) Time | O(wh) Space - width, height of matrix

##################
Detailed explanation of the Solution:
# function - riversizes for matrix:
    Initialize sizes as list to hold the rivers
    Initializing visited as "2D matrix to False" - False for value in row and for row in matrix

    loop as i for range len in the matrix:
        loop as j in range of len matrix for i:
            if visited i j: # if the node has been visited, continue or if visited[i][j] == True
                continue
            traverseNode for i, j, matrix, visited, sizes # if the node has not been visited, traverse the node
    return sizes # of the array as initialized before

# function - traverseNode(i, j, matrix, visited, sizes)
    intialize the currentRiverSize to be 0
    initialize nodesToExplore to be [[i, j]] # queue

    while there is length of nodesToExplore: # while there are nodes to explore
        initialize currentNode to pop the element in the nodesToExplore # pop first element from the queue
        initialize i as currentNode for first index # get the row
        initialize j as currentNode for second index # get the row
        if visited i j: # if the node has been visited
            continue
        mark visited i j is equal to True # mark the node as visited
        if matrix i j equilized to 0 # if the node is 0
            continue
        increment currentRiverSize by 1 #  this will add it to the queue
        initialize unvisitedNeighbors equal to getUnvisitedNeighbors for i, j, matrix, visited # get the unvisited neighbors
        iterate through the unvisitedNeighbors as neighbor:
            append neighbor to the nodesToExplore # add the neighbor to the queue
    if the currentRiverSize is greater than the 0:
        add the currentRiverSize to the sizes

# function ​- getUnvisitedNeighbors(i, j, matrix, visited):
    unvisitedNeighbors is equal to [] # list to store the neighbors
    numRows is equal to lenOfMatrix
    numCols is equal to lenOfMatrix for row

    if i-1 is greater than and equal to 0: # UP # check if the row is not on the border
        unvisitedNeighbors.append([i - 1, j]) # push the neighbor into the neighbors list
    if i+1 is less than numRows: # DOWN # check if the row is not on the border
        unvisitedNeighbors.append([i + 1, j]) # push the neighbor into the neighbors list
    if j-1 is greater than and equal to 0: # LEFT # check if the column is not on the border
        unvisitedNeighbors.append([i, j - 1]) # push the neighbor into the neighbors list
    if j+1 is less than numCols: # RIGHT # check if the column is not on the border
        unvisitedNeighbors.append([i, j + 1]) # push the neighbor into the neighbors list

    return unvisitedNeighbors
"""
####################################

def riverSizes(matrix):
    sizes = [] # holds the sizes of the rivers
    visited = [[False for value in row] for row in matrix] # initializing visited as "2D matrix to False" - False for value in row and for row in matrix

    # iterate through the matrix row by row and check if the element is 1 # if it is 1, add it to the queue # if it is 0, add it to the queue
    for i in range(len(matrix)): # iterate through the rows
        for j in range(len(matrix[i])): # iterate through the rows for i
            if visited[i][j]: # if the node has been visited, continue or if visited[i][j] == True
                continue
            traverseNode(i, j, matrix, visited, sizes) # if the node has not been visited, traverse the node
    return sizes

def traverseNode(i, j, matrix, visited, sizes): # i and j are rows
    currentRiverSize = 0 # holds the size of the river
    # depth first search # stack
    nodesToExplore = [[i, j]] # holds the nodes to explore # stack
    while len(nodesToExplore): # while there are nodes to explore
        currentNode = nodesToExplore.pop() # pop the first node from the queue
        i = currentNode[0] # get the row
        j = currentNode[1] # get the row
        if visited[i][j]: # if the node has been visited, continue
            continue
        visited[i][j] = True # mark the node as visited
        if matrix[i][j] == 0:
            continue
        currentRiverSize += 1 # increment the river size # if the node is 1, add it to the queue
        unvisitedNeighbors = getUnvisitedNeighbors(i, j, matrix, visited)
        for neighbor in unvisitedNeighbors:
            nodesToExplore.append(neighbor) # add the neighbor to the queue
    if currentRiverSize > 0: # if the river size is greater than 0
        sizes.append(currentRiverSize) # add the river size to the sizes array

def getUnvisitedNeighbors(i, j, matrix, visited):
    unvisitedNeighbors = []
    numRows = len(matrix)
    numCols = len(matrix[i])

    if i - 1 >= 0: # UP # check if the row is not on the border
        unvisitedNeighbors.append((i - 1, j)) # push the neighbor into the neighbors list
    if i + 1 < numRows: # DOWN # check if the row is not on the border
        unvisitedNeighbors.append((i + 1, j))
    if j - 1 >= 0: # LEFT # check if the col is not on the border
        unvisitedNeighbors.append((i, j - 1)) #
    if j + 1 < numCols: # RIGHT # check if the col is not on the border
        unvisitedNeighbors.append((i, j + 1))
        
    return unvisitedNeighbors

def main():
    matrix = [
        [1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0],
    ]
    print(riverSizes(matrix)) # [1, 2, 2, 2, 5]

if __name__ == '__main__':
    main()