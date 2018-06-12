# Completely inadequate
# Need to take time to complete this entire assignment

list = [4,3,5,6,1,2,8,9,0,7]


def selection_sort(arr):
    length = len(arr)
    minVal = min(arr)

    for i in arr:
        if arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i+1], arr[i]
        print(list)

    # newArr = []

selection_sort(list)