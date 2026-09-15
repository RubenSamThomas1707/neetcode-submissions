class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Brute force approach
            # for each cell (r, c) in board:
            #     if board[r][c] == ".":
            #         continue
                
            #     val = board[r][c]

            #     # check row
            #     for each column j in 0..8:
            #         if j != c and board[r][j] == val:
            #             return False

            #     # check column
            #     for each row i in 0..8:
            #         if i != r and board[i][c] == val:
            #             return False

            #     # check 3x3 sub-box
            #     boxRowStart = (r // 3) * 3
            #     boxColStart = (c // 3) * 3
            #     for i in boxRowStart..boxRowStart+2:
            #         for j in boxColStart..boxColStart+2:
            #             if (i, j) != (r, c) and board[i][j] == val:
            #                 return False
        
        # ------------------------------------

        # Best Solution:
            # Create a row list of 9 sets - Keep track of non-duplicates in each row
            # Create a column list of 9 sets - Keep track of non-duplicates in each column
            # Create a box list of 9 sets - Keep track of non-duplicates in each box
            # Create loop to iterate through rows
                # Create loop to iterate through columns
                    # Check if element is a "." (emty spot)
                        # continue without doing anything
                    # Check if element exists in the row set
                        # if no then add it to the row set at that index
                        # Else return false

                    # Check if element exists in the column set
                        # if no then add it to the column set at that index
                        # Else return false

                    # Calculate the box number formula = ((row // 3) * 3 + (column // 3))
                    # ** ^ formula would help calculate a single box value to be used as index
                    # ** for all values in a single box

                    # Check if element exists in the box set
                        # If no then add it to the box set at that index
                        # Else return false
                    
            # Return true indicating that the board is valid
        
        # ------------------------------------
        # rows = [set() for _ in range(9)]
        # cols = [set() for _ in range(9)]
        # boxes = [set() for _ in range(9)]

        # for row in range(len(board)):
        #     for col in range(len(board[0])):
        #         currVal = board[row][col]

        #         if currVal != ".":
        #             if currVal in rows[row]:
        #                 return False
        #             else:
        #                 rows[row].add(currVal)
                    
        #             if currVal in cols[col]:
        #                 return False
        #             else:
        #                 cols[col].add(currVal)
                    
        #             currBox = (row // 3) * 3 + (col // 3)
        #             if currVal in boxes[currBox]:
        #                 return False
        #             else:
        #                 boxes[currBox].add(currVal)
        
        # return True

        rows = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board[0]))]
        subboxes = [set() for _ in range(9)]

        for row in range(len(board)):
            for col in range(len(board[0])):
                currElem = board[row][col]

                if currElem == '.':
                    continue
                
                subboxIndex = (row // 3) * 3 + (col // 3)

                if (currElem in rows[row]) or (currElem in cols[col]) or (currElem in subboxes[subboxIndex]):
                    return False
                
                rows[row].add(currElem)
                cols[col].add(currElem)
                subboxes[subboxIndex].add(currElem)
        
        return True









                    