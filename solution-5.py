# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    east = 0
    passing = 0
    for car in A:
        if car == 0: #count cars going east
            east +=1 
        else:
            passing +=east 
        if passing > 1000000000:
            return -1
    return passing