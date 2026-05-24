#bai1
def permutations(nums):
    result = []
    def backtrack(path, remaining):     #base case
        if len(path) == len(nums):
            result.append(path.copy())
            return
        for i in range(len(remaining)):
            path.append(remaining[i])
            backtrack(path, remaining[:i] + remaining[i+1:])
            path.pop()
    backtrack([], nums)
    return result
print(permutations([1, 2, 3]))
result = permutations([1, 2, 3])
print(f"hoán vị của [1, 2, 3]: {result}")
print(f"tổng số hoán vị: {len(result)}")

#bai2
def is_safe(board, row, col, n):
    """
    kiểm tra đặt quân hậu ở(row, col) có hợp lệ không
    board: danh sách vị trí cột của quân hậu ở mỗi hàng
    """
    for prev_row in range(row):
        prev_col = board[prev_row]
        if prev_col == col:
            return False
        if abs(prev_row - row) == abs(prev_col - col):
            return False
    return True

def solve_n_queens(n):
    """
    tìm tất cả cách đặt N quân hậu
    """
    result = []
    board = [] 
    def backtrack(row):
        if row == n:
            result.append(board.copy())
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board.append(col)
                backtrack(row + 1)
                board.pop()
    backtrack(0)
    return result

def print_board(solution, n):
    """
    in bàn cờ NxN với quân hậu
    solution: danh sách [col0, col1, ..., colN-1]
    """
    for row in range(n):
        line = ""
        for col in range(n):
            if solution[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
        print()
solution = solve_n_queens(4)
print(f"tìm thấy {len(solution)} giải pháp: ")
for i, sol in enumerate(solution):
    print(f"giải pháp {i + 1}:")
    print_board(sol, 4)

import time
def compare_n_queens(n):
    print(f"\n{'='*50}")
    print(f"so sánh N-Queens với N={n}")
    print(f"{'='*50}")
    print("\n[1]KHÔNG có pruning: ")
    start = time.time()
    result1 = solve_n_queens(n)
    time1 = time.time() - start
    print(f"thời gian: {time1:.6f}s ")
    print("\n[2] CÓ pruning: ")
    start = time.time()
    result2 = solve_n_queens(n)
    time2 = time.time() - start
    print(f"thời gian: {time2:.6f}s ")
    print(f"\ntốc độ tăng: {time1/time2:.2f}x")
    if len(result2) > 0:
        print(f"\nmột giải pháp cho {n}-Queens: ")
        print_board(result2[0], n)
compare_n_queens(4)
compare_n_queens(8)

#bai3
def subset_sum(nums, target):
    result =[]
    def backtrack(start, path, current_sum):
        if current_sum == target:
            result.append(path.copy())
            return
        if current_sum > target:
            return
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path, current_sum + nums[i])
            path.pop()
    backtrack(0, [], 0)
    return result
print(subset_sum([2, 3, 5, 7], 7))