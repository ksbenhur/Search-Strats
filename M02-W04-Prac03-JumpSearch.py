import math

def jump_search(array, x, n):
    s = math.sqrt(n)
    p = 0
    while array[int(min(s, n)-1)] < x:
        p = s
        s += math.sqrt(n)
        if p >= n:
            return -1
    while array[int(p)] < x:
        p += 1
        if p == min(s, n):
            return -1
    if array[int(p)] == x:
        return p
     
    return -1


if __name__ == '__main__':

    int_arr = list(map(int, input().split(' ')))
    target = int(input())
    
    # Function call
    result = jump_search(int_arr, target, len(int_arr) - 1)

    if result != -1:
        print("Element is present at index ", int(result))
    else:
        print("Element is not present in array")