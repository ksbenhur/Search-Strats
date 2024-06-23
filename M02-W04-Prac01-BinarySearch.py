# Python Program for recursive binary search.

# Returns index of x in arr if present, else -1
def binary_search(arr, l, r, target):
    if r>=l:
        mid=l+(r-1)//2
        for i in range(len(arr)):
            if target == arr[mid]:
                return mid
            elif target<arr[mid]:
                return binary_search(arr,l,mid-1,target)
            else:
                return binary_search(arr,mid+1,r,target)
    else:
        return -1  

if __name__ == "__main__":
    # Test array
    int_arr = list(map(int, input().split(' ')))
    n = len(int_arr)
    target = int(input())
    
    # Function call
    result = binary_search(int_arr, 0, len(int_arr) - 1, target)

    if result != -1:
        print("Element is present at index %d" % result)
    else:
        print("Element is not present in array")