#bai1
def snipper_0():
    a = 3
    b = 4
    c = a + b
    return c           #khong phu thuoc n -- O(1)

def snipper_1(n):
    total = 0
    for i in range(n): #lap n lan - O(n)
        total += i
    return total       #vong lap chay n lan - moi lan co 1 phep gan or cong

def snipper_2(n):
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count      #voi moi vong ngoai chay n lan - vong trong chay n lan - O(n^2) 

def snipper_3(n):
    count = 0
    while n > 0:     #kiem tra n > 0 -- n = n chia 2 -- count tang len 1
        count += 1
        n = n // 2
    return count     #vong lap chay log(n) lan - O(log n)

#bai2
def snipper_4(n):
    total = 0
    for i in range(n):
        for j in range(n):    
            total += 1
        return total          #-O(n^2)

def snipper_5(n):
    k = 1
    total = 0
    while k < n:
        for i in range(n):
            total += 1
        k = k * 2
    return total         #-O(n log n)   

#bai3
#phan tich 1 ham co do phuc tap O(n^2)
def two_sum_n1(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                return True
    return False

#viet lai 1 ham co do phuc tap O(n)
def two_sum_n2(arr):
    seen = set()
    for item in arr:
        if item in seen:
            return True
        seen.add(item)
    return False

#so sanh thoi gian
import time
arr = list(range(100000))
arr.append(5000)
start = time.time()    #-cach 1
result1 = two_sum_n1(arr)
time1 = time.time() - start
print(f"Cach 1: {time1:.4f} giay")             

start = time.time()   #-cach 2
result2 = two_sum_n2(arr)
time2 = time.time() - start
print(f"Cach 2: {time2:.4f} giay")             

#bai toan
def two_sum(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return (i, j)
    return None
arr = [1, 3, 4, 6, 7, 8, 10]
target = 10
print(two_sum(arr, target))