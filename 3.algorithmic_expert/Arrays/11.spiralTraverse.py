# Problem Name: Spiral Traverse

# Problem Description:
# Write a function that takes an n x m two-dimendional array (that can be square-shaped when n == m) and returns a one-dimensional array of all array's elements in spiral order.

# Spiral order starts at the top left corner of the two-dimensional array, goes to the right, and proceeds in a spiral pattern all the way until every element has been visited.

####################################
# Sample Input:
# array =  [
#     [1, 2, 3, 4],
#     [12, 13, 14, 5],
#     [11, 16, 15, 6],
#     [10, 9, 8, 7]
#   ]
# Sample Output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

####################################
"""
Explain the solution:
1- You can think of the spiral that you have to traverse as a set of rectangle perimeters that progressively get smaller and smaller(i.e that progressively move inwards in the two-dimensional array).

2- Going off of Hint #1, declare four variables: a starting row, a starting column, an ending row, and an ending column. These four variables represent the bounds of the first rectangle perimeter in the spiral that you have to traverse. Traverse that perimeter using those bounds, and then move the bounds inwards. End your algorithm once the starting row passes the ending row or the starting column passes the ending column.

3- You can solve this problem both iteratively and recursively following very similar logic.

# O(n) time | O(n) space - where n is the total number of elements in the array

##################
Detailed explanation of the Solution:

create a function for spiralTraverseIteratively to take the parameters of the array:
    result = []
    startRow = 0
    startCol = 0
    endRow = len(array) - 1
    endCol = len(array[0]) - 1

    while startRow <= endRow and startCol <= endCol:
        # Traverse the top row
        for col in range(startCol, endCol + 1): # why endCol + 1? because we want to include the last element in the row
            result.append(array[startRow][col])

        # Traverse the right column
        for row in range(startRow + 1, endRow + 1): 
            result.append(array[row][endCol])

        # Traverse the bottom row
        for col in reversed(range(startCol, endCol)):
            # Handle the edge case when there's a single row in the middle of the matrix. In this case, we don't want to double-count the values in this row, which we've already counted in the first loop above.
            if startRow == endRow:
                break
            result.append(array[endRow][col])

        # Traverse the left column
        for row in reversed(range(startRow + 1, endRow)):
            # Handle the edge case when there's a single row in the middle of the matrix. In this case, we don't want to double-count the values in this column, which we've already counted in the second for loop above.
            if startCol == endCol:
                break
            result.append(array[row][startCol])

        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1
    return result
"""
####################################
# O(n) time | O(n) space - where n is the total number of elements in the array.

# iterative solution

def spiralTraverseIteratively(array):
    result = []
    startRow = 0
    startCol = 0
    endRow = len(array) - 1
    endCol = len(array[0]) - 1

    while startRow <= endRow and startCol <= endCol:
        # Traverse the top row
        for col in range(startCol, endCol + 1):
            result.append(array[startRow][col])
        
        # Traverse the right column
        for row in range(startRow + 1, endRow + 1):
            result.append(array[row][endCol])

        # Traverse the bottom row
        for col in reversed(range(startCol, endCol)):
        # Handle the edge case when there's a single row in the middle of the matrix. In this case, we don't want to double-count the values in this row, which we've already counted in the first loop above. 
            if startRow == endRow:
                break
            result.append(array[endRow][col])
        
        # Traverse the left column
        for row in reversed(range(startRow + 1, endRow)):
            # Handle the edge case when there's a single row in the middle of the matrix. In this case, we don't want to double-count the values in this column, which we've already counted in the second for loop above.
            if startCol == endCol:
                break
            result.append(array[row][startCol])

        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1
    return result

print(spiralTraverseIteratively([
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
  ]))

# recursive solution

def spiralTraverseRecursively(array):
    result = []
    spiralFill(array, 0, len(array) - 1, 0, len(array[0]) - 1, result)
    return result

def spiralFill(array, startRow, endRow, startCol, endCol, result):
    if startRow > endRow or startCol > endCol:
        return
    # copy the logic of the iterative solution from here
    for col in range(startCol, endCol + 1):
        result.append(array[startRow][col])
    for row in range(startRow + 1, endRow + 1):
        result.append(array[row][endCol])
    for col in reversed(range(startCol, endCol)):
        if startRow == endRow:
            break
        result.append(array[endRow][col])
    for row in reversed(range(startRow + 1, endRow)):
        if startCol == endCol:
            break
        result.append(array[row][startCol])
   # to here
    spiralFill(array, startRow + 1, endRow - 1, startCol + 1, endCol - 1, result)


# print(spiralTraverseRecursively([
#     [1, 2, 3, 4],
#     [12, 13, 14, 5],
#     [11, 16, 15, 6],
#     [10, 9, 8, 7]
#     ]))
