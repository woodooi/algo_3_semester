def can_fit_all(n, w, h, board_size):

    row = board_size // w
    col = board_size // h
    total_leaves = row * col
    return total_leaves >= n

def min_board_size(num_of_leaves, width, height):

    left = min(width, height)
    right = max(width, height) * num_of_leaves
    result = right 
    count = 0 

    while left <= right:
        mid = (left + right) // 2
        if can_fit_all(num_of_leaves, width, height, mid):
            result = mid  
            right = mid - 1  
        else:
            left = mid + 1  
        count += 1
    
    print(count)
    return result

if __name__ == '__main__':
    result = min_board_size(9000, 1000000000, 999999999)
    print(f'Minimum board size => {result}x{result}')