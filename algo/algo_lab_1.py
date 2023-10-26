"""Contains class Solution"""
class Solution:
    """
    Contains zig zag function
    """
    def __init__(self, m: []) -> None:
        self.matrix = m
    
    def zig_zagging(self):
        """
        Zig-zagger
        """
        if not self.matrix:
            return []
        
        result = []    
        row, col = len(self.matrix) - 1, len(self.matrix[0]) - 1
        current_row, current_column = 0, 0 
        iter_up = True
        
        while (current_row < row + 1 and current_column < col + 1):
            result.append(self.matrix[current_row][current_column])

            if iter_up:
                if current_row > 0 and current_column != col:
                    current_row -= 1
                    current_column += 1 
                elif current_column == col:
                    current_row += 1
                    iter_up = False 
                elif current_row == 0:
                    current_column += 1
                    iter_up = False
            else:
                if current_row == row:
                    current_column += 1
                    iter_up = True
                elif current_row < row and current_column > 0:
                    current_column -= 1
                    current_row += 1
                elif current_column == 0:
                    current_row += 1
                    iter_up = True
        
        return result

matrix = Solution([
    [1, 2, 3, 4, 5],
            [6,7,8,9,10],
            [11,12,13,14,15],
            [16,17,18,19,20],
            [21,22,23,24,25]
])

matrix2 = Solution([
            [1, 2, 3, 4],
            [5, 6, 7, 8]
            ])

print("x")
result = matrix.zig_zagging()
print(result)
print("x")
result2 = matrix2.zig_zagging()
print(result2)
print("x")
