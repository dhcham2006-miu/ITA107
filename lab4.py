#bai1
#activity selection - chọn hoạt động tối đa
def activity_selection(activities):
    activities.sort(key=lambda x: x[1])
    selected = [activities[0]]
    last_finish = activities[0][1]
    for i in range(1, len(activities)):
        start, finish = activities[i]
        if start >= last_finish:
            selected.append((start, finish))
            last_finish = finish
    return selected
print("===test activity selection ===")
activities = [(1, 3), (2, 5), (4, 7), (1, 8), (5, 9), (8, 10)]
result = activity_selection(activities)
print(f"hoạt động được chọn: {result}")
print(f"số lượng: {len(result)}")        #O(n log n)
#coin change greedy - đổi tiền tham lam
def coin_change_greeedy(amount, coins):
    coins.sort(reverse=True)
    count = 0
    result = [1]
    for coin in coins:
        while amount >= coin:
            result.append(coin)
            amount -= coin
    if amount == 0:
        return len(result), result
    else:
        return -1, []
print("\n=== test coin change greedy ===")
print("test: hệ tiền chuẩn [25, 10,5 1]")
amount = 63
coins = [25,10, 5, 1]
count, result = coin_change_greeedy(amount, coins)
print(f"số tiền: {amount}")
print(f"số xu: {count}")
print(f"chi tiết: {result}")

#bai2
import heapq
from http import cookies
def min_meeting_rooms(meetings):
    if not meetings:
        return 0
    meetings.sort(key=lambda x: x[0])
    heap = []
    heapq.heappush(heap,meetings[0][1])
    for i in range(1, len(meetings)):
        start, end = meetings[i]
        if start >= heap[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, end)
    return len(heap)
meetings = [(0, 30), (5, 10), (15, 20)]
print(min_meeting_rooms(meetings))

#bai3
def find_content_chilren(greed, cookie):
    """
    Assing Coodie - LeetCode 455
    """
    
    greed.sort()
    cookie.sort()
    i = 0
    j = 0
    while i < len(greed) and j < len(cookie):
        if cookie[j] >= greed[i]:
            i += 1
        j += 1
    return i
greed1 = [1, 2, 3]
cookies1 = [1, 1]
print(find_content_chilren(greed1, cookies1))  