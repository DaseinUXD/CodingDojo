# Assignment: Type List
# Write a program that takes a list and prints a message for each element in the list,
# based on that element's data type.   Your program input will always be a list. For each item in the list, test
# its data type. If the item is a string, concatenate it onto a new string. If it is a number, add it to a running sum.
#  At the end of your program print the string, the number
# and an analysis of what the list contains. If it contains only one type, print that type, otherwise, print 'mixed'.
# # Here are a couple of test cases. Think of some of your own, too. What kind of unexpected input could you get?

def typeList(l):
    for i in l:

        isIntMixed = isinstance(i, int)
        isStrMixed = isinstance(i, basestring)
        isInt = isinstance(i, int)
        isStr = isinstance(i, basestring)
        mixTypeEval = []
        mixTypeEval.append(isIntMixed)
        mixTypeEval.append(isStrMixed)
        numTypeEval = []
        numTypeEval.append(isInt)
        strTypeEval=[]
        strTypeEval.append(isStr)

    # print numTypeEval
    # print strTypeEval
    # print mixTypeEval

    if all(numTypeEval):
        print "List is all numbers"
    elif all(strTypeEval):
        print "List is all strings"
    else:
        all(mixTypeEval)
    print "this is a mixed list"

typeList(['magical unicorns',19,'hello',98.98,'world'])

typeList([2,3,1,7,4,12])

typeList(['magical','unicorns'])





#input
#l = ['magical unicorns',19,'hello',98.98,'world']
#output
"The list you entered is of mixed type"
"String: magical unicorns hello world"
"Sum: 117.98"


# input
#l = [2,3,1,7,4,12]
#output
"The list you entered is of integer type"
"Sum: 29"


# input
#l = ['magical','unicorns']
#output
"The list you entered is of string type"
"String: magical unicorns"
