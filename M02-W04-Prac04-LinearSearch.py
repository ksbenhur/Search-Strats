# Returns index of x in arr if present, else -1
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
        else:
            continue
    return -1


if __name__ == "__main__":
    # Test array
    int_arr = list(map(int, input().split(' ')))
    target = int(input())
    
    # Function call
    result = linear_search(int_arr, target)

    if result != -1:
        print("Element is present at index ", result)
    else:
        print("Element is not present in array")