class Solution:
    # @param A : list of list of chars
    # @return nothing
    def solveSudoku(self, A):
        #Function to initialize 'row' and 'col' hash-maps
        def initialize():
            for i in range(9):
                row[i] = {}
                col[i] = {}
                grid[i] = {}
            for i in range(9):
                for j in range(1,10):
                    row[i][j] = 0
                    col[i][j] = 0
                    grid[i][j] = 0
            
        def gNum(i, j):
            if i >= 0 and i <= 2:
                if j >= 0 and j <= 2:
                    return(0)
                if j >= 3 and j <= 5:
                    return(1)
                if j >= 6 and j <= 8:
                    return(2)
            if i >= 3 and i <= 5:
                if j >= 0 and j <= 2:
                    return(3)
                if j >= 3 and j <= 5:
                    return(4)
                if j >= 6 and j <= 8:
                    return(5)
            if i >= 6 and i <= 8:
                if j >= 0 and j <= 2:
                    return(6)
                if j >= 3 and j <= 5:
                    return(7)
                if j >= 6 and j <= 8:
                    return(8)

        def markFilledNums():
            for i in range(9):
                for j in range(9):
                    if A[i][j] != '.':
                        row[i][int(A[i][j])] = 1
                        col[j][int(A[i][j])] = 1
                        grid[gNum(i, j)][int(A[i][j])] = 1

        def findVacantCells():
            for i in range(9):
                for j in range(9):
                    if A[i][j] == '.':
                        vacant.append([i,j])

        def sudoku(pos):
            i, j = vacant[pos][0], vacant[pos][1]
            for num in range(1,10):
                if row[i][num] == 0 and col[j][num] == 0 and grid[gNum(i,j)][num] == 0:
                    A[i][j] = str(num)
                    row[i][num] = 1
                    col[j][num] = 1
                    grid[gNum(i,j)][num] = 1
                    #filledCell = vacant.pop()
                    if pos == len(vacant) - 1:
                        return(True)
                    extendSoln = sudoku(pos + 1)
                    if extendSoln:
                        return(True)
                    else:
                        A[i][j] = '.'
                        row[i][num] = 0
                        col[j][num] = 0
                        grid[gNum(i,j)][num] = 0
                        #vacant.append(filledCell)
            else:
                return(False)

        row, col, grid = {}, {}, {}
        vacant = []
        initialize()
        markFilledNums()
        findVacantCells()
        sudoku(0)
