# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    N = len(A)+1
    total = 0
    for num in range(1, N+1):
        total += num
    for num in A:
        total -=num
    return total