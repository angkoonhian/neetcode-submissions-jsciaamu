class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            # Check if there are vertical duplicates
            vertical_map = {}
            for row in board:
                if row[i] != ".":
                    if row[i] in vertical_map:
                        return False
                    vertical_map[row[i]] = 1

            # Check if there are horizontal duplicates - done within rows, refresh within rows
            horizontal_map = {}
            # populate maps
            for num in board[i]:
                if num != ".":
                    if num in horizontal_map:
                        return False
                    horizontal_map[num] = 1

            # Check grid duplicates
            grid_map = {}
            curr_horizontal_index = i // 3
            for j in range(3):
                for x in range(3):
                    final_horizontal_index = curr_horizontal_index * 3 + x 
                    num = board[j][final_horizontal_index]
                    if num != ".":
                        if num in grid_map:
                            return False
                        grid_map[num] = 1

        return True
        