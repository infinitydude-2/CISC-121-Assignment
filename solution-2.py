# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    counts = {}

    for num in A:
        if num in counts:
            counts[num]+=1
        else:
            counts[num] = 1
    for num in counts:
        if counts[num] %2 != 0:
            return num