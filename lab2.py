#bai 1
#base case - dieu kien de dung, truong hop nho nhat
#recursive case - phan goi lai chinh no, chia nho van de
#tinh tong 1+2+...+n
def sum_to_n(n):
    if n == 0 or n == 1: #base case 
        return n         #recursive case
    return n + sum_to_n(n - 1)
print(sum_to_n(5))   
print(sum_to_n(10))
# tinh n mu k ( power)
def power(n, k):
    if k == 0:                  #base case
        return 1
    return n * power(n, k - 1)   #recursive case
print(power(2, 3))

#bai 2
# fibonacci de quy don gian
def fib_slow(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_slow(n - 1) + fib_slow(n - 2)
print("Fibonacci naive: ")
print(fib_slow(10))
print(fib_slow(20))      #O(2^n) - rat cham khi n lon

#fibonacci voi memoization
def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 0:
        memo[0] = 0
    elif n == 1:
        memo[1] = 1
    else:
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]
print("fibonacci memoization: ")
print(fib_memo(10))
print(fib_memo(50))      #O(n) - nhanh hon nhieu khi

#test time
import time
start = time.time()
a = fib_slow(30)
end = time.time()
print(f"fib_slow: {end - start:.4f} giay")

start = time.time()
b = fib_memo(30)
end = time.time()
print(f"fib_memo: {end - start:.4f} giay")


#bai 3
#merge sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("mang ban dau:", arr)
print("mang sau khi sap xep:", sorted_arr)