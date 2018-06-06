# Countdown - Create a function that accepts a number as an input.  Return a new array that counts down by one, from the
# number (as arrays 'zero'th element) down to 0 (as the last element).
# For example countDown(5) should return [5,4,3,2,1,0].

def count_down(num):
    arr = []
    for i in range(num, -1, -1):
        print(i)
        arr.append(i)
    print(arr)


count_down(5)


# Print and Return - Your function will receive an array with two numbers. Print the first value, and return the second.

def print_return(arr):
    print(arr[0])
    return arr[1]


print(print_return([2, 3]))


# First Plus Length - Given an array, return the sum of the first value in the array, plus the array's length.
def first_plus_length(arr):
    first = arr[0]
    print(first)
    length = len(arr)
    print(length)
    sum = first + length
    return sum


print(first_plus_length([4, 5, 6, 7, 3, 4, 9]))


# Values Greater than Second - Write a function that accepts any array, and returns a new array with the array values
# that are greater than its 2nd value.  Print how many values this is.
# If the array is only element long, have the function return False
def value_greater(array):
    # print(array)
    newArray = []
    count = 0
    if len(array) > 1:
        for i in range(0,len(array),1):
            # print(i)
            # val = array[i]
            # test = array[1]
            # print(array[i])
            if array[i] > array[1]:
                count = count +1
                # print(count)
                newArray.append(array[i])
                # print(newArray)
        return newArray, count
    else:
        return False
print(value_greater([2,3,4,5,6,1,2,1]))

# This Length, That Value - Given two numbers, return array of length num1 with each value num2.
# Print "Jinx!" if they are same.

def this_length_that_value(a, b):
    newArray=[]
    if a != b:
        for i in range(a):
            # print(i)
            newArray.append(b)
        print(newArray)
    else:
        print("Jinx!")
this_length_that_value(9,2)
