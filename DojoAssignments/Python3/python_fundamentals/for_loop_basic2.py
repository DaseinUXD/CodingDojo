# For Loop Basic II
# Objectives
# Get comfortable writing functions only using basic building blocks of Python (we want you to gain confidence in your
#  ability to write custom functions instead of relying too heavily on advanced built in python functions
# Get comfortable using for loops, functions, lists, and other data types
#
# Biggie Size - Given an array, write a function that changes all positive numbers in the array to "big".
#     Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5].
def biggie_size(array):
    for i in range(0, len(array), 1):
        # print(i)
        # print(array[i])
        if array[i] > 0:
            array[i] = 'Big'
            # print(array[i])
    # print(array)
    return array


print(biggie_size([-1, 3, 5, -5]))


# Count Positives - Given an array of numbers, create a function to replace last value with number of positive values.
#   Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.  (Note that zero is not considered to b a positive number).
def count_positives(array):
    count = 0
    for i in range(len(array)):
        if array[i] > 0:
            count = count + 1
    array[len(array) - 1] = count
    # print(array)
    # print(count)
    return count, array


print(count_positives([2, 2, -1, -2, 3, -4]))


# SumTotal - Create a function that takes an array as an argument and returns the sum of all the values in the array.
#   For example sumTotal([1,2,3,4]) should return 10
def sum_total(array):
    sum = 0
    for i in range(len(array)):
        # print(i)
        # print(array[i])
        sum = sum + array[i]
    # print(sum)
    return sum


print(sum_total([2, 4, 8, 4, 5, 6]))


# Average - Create a function that takes an array as an argument and returns the average of all the values in the array.
#   For example multiples([1,2,3,4]) should return 2.5
def average(array):
    sum = 0
    n = len(array)
    for i in range(n):
        sum = sum + array[i]
    # print(sum / n)
    return sum / n


print(average([1, 2, 3, 4, 5, 6, 7, 8, 9]))


# Length - Create a function that takes an array as an argument and returns the length of the array.
#   For example length([1,2,3,4]) should return 4

def length(array):
    arrayLength = len(array)
    # print(arrayLength)
    return arrayLength


print(length([1, 2, 3, 4]))


# Minimum - Create a function that takes an array as an argument and returns the minimum value in the array.
#   If the passed array is empty, have the function return false.
#     For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.
def minimum(array):
    minVal = 0
    for i in range(len(array)):
        if array[i] > array[i - 1]:
            array[i] = array[i - 1]
            minVal = array[i]
        if len(array) == 0:
            return False
    # print("The minimum value in the list is: " + str(minVal))
    return minVal


print('The minimum value is: ' + str(minimum([-1, 3, -8, -3])))


# Maximum - Create a function that takes an array as an argument and returns the maximum value in the array.
#   If the passed array is empty, have the function return false.
#   For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -3.
def maximum(array):
    maxVal = 0
    for i in range(len(array)):
        # print(i)
        if array[i] < array[i - 1]:  # the lt and gt symbols are the only differences in these functions
            array[i] = array[i - 1]
            maxVal = array[i]
        if len(array) == 0:
            return False
    # print("The maximum value in the list is: " + str(maxVal))
    return maxVal


print('The maximum value is: ' + str(maximum([1, 3, 5, 6, -9, 22])))


# UltimateAnalyze - Create a function that takes an array as an argument and returns a dictionary that has the
#  sumTotal, average, minimum, maximum and length of the array.

def ultimate_analyze(list):
    dictionary = {
        'sum_total': sum_total([1, 3, 5, 6, -9, 22]),
        'average': average([1, 3, 5, 6, -9, 22]),
        'minimum': minimum([1, 3, 5, 6, -9, 22]),
        'maximum': maximum([1, 3, 5, 6, -9, 22]),
        'array_length': length([1, 3, 5, 6, -9, 22]),
    }

    return dictionary


print(ultimate_analyze([1, 3, 5, 6, -9, 22]))


# ReverseList - Create a function that takes an array as an argument and return an array in a reversed order.
#   Do this without creating an empty temporary array.
#   For example reverse([1,2,3,4]) should return [4,3,2,1].
#   This challenge is known to appear during basic technical interviews.

def reverse(arr):
    temp = 0
    # print(len(arr))
    # print(len(arr))

    # for i in range(0, len(arr), 1):
    for i in range(len(arr)):
        if len(arr) % 2==0:

            print(i)
            first = arr[i]
            last = first
            print(last)
            midLeft = arr[(i+1)]
            print(midLeft)
            midRight = arr[-(1+i)]
            print(midRight)
            last = arr[-1]
            print(last)
            first = last
            print(first, last)
            # print(arr[0])
        print(arr)



#         # print(i)
#         # n = len(arr)
#         # print(n)
#         # while i <= n:
#         # print(i)
#         first = arr[-i+i]  # set the variable first to the value at array[i] which initially is array[0]
#         # print(first)
#         last = arr[len(arr) - 1-i]  # set the variable last to the value at last index in the array: array[len(arr)-1] (i.e., array[-1])
#         # print(last)
#         arr[-i+i] = last  # set the value at array[i] to shift (which was the placeholder for the value at the last index
#         # print(arr[-i+i])
#         # shift = last # set the variable shift to the last value to hold it while we swap places
#         # print(shift)
#         # print(first)
#         arr[len(arr) - 1-i] = first  # set the last index in the array to variable
#         # print(arr[len(arr) - 1-i])
#         # i = i + 1
#     # print(arr)
#
#
# # print(arr)
#
#     # for i in range(len(arr)):
#     #     arr[i]
#     #
#     # return
#

reverse([2, 4, 6, 7])
