# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    for i in range(K):
        if len(A)>0:
            last = A[-1]
            A.pop()
            A.insert(0,last)

    return A
