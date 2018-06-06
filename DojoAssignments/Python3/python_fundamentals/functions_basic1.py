# Predict the output of the codes below without running the codes directly.
# Write down your predictions for all challenges below and once done, please compare your predictions with the results from the shell.

def a():
    return 5
print(a())  # 5 -> correct

def a():
    return 5
print(a()+a()) # 10 -> Correct
#
def a():
    return 5
    return 10
print(a())    # 5 -> correct
#
def a():
    return 5
    print(10)
print(a())    # 5 -> correct
#
def a():
    print(5)
x = a()
print(x)     # 5, None -> correct
#
def a(b,c):
    print(b+c) # 3, 5  -> correct
print((a(1,2)) + a(2,3)) # 8 -> incorrect
#
def a(b,c):
    return str(b)+str(c)
print(a(2,5)) # '2','5' -> incorrect // correct -> 25
#
def a():
    b = 100
    print(b) # 100
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a) # None -> incorrect // correct -> <function a at memorylocation>
#
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3)) # 7 -> correct
print(a(5,3)) # 14 -> correct
print(a(2,3) + a(5,3)) # 21 -> correct

def a(b,c):
    return b+c
    return 10
print(a(3,5)) # 8 -> correct
b = 500
print(b) # 500 -> correct

def a():
    b = 300
    print(b) # 300 -> correct
print(b) # Unresolved reference 'b' is not defined -> correct
a() # function a at memory location -> incorrect // did not return anything???
print(b) # Unresolved reference 'b' is not defined-> correct
b = 500
print(b) # 500 -> correct
#
def a():
    b = 300
    print(b) # 300 -> correct
    return b # will do nothing -> correct
# print(b) # Unresolved reference 'b' is not defined -> correct
a()
# print(b) # Unresolved reference 'b' is not defined  -> correct
b = 500
print(b) # 500 -> correct
#
def a():
    b = 300
    print(b) # 300 -> correct
    return b # will do nothing now -> correct
# print(b) # Unresolved reference 'b' is not defined -> correct
b=a() # will do nothing -> correct
print(b) # 300?  -> correct
#
def a():
    print(1) # 1 -> correct
    b() #3 -> correct
    print(2) # 2 -> correct
def b():
    print(3) # nothing
a()

def a():
    print(1) # 1 -> correct
    x = b() # 3 -> correct
    print(x) # 5 -> correct
    return 10
def b():
    print(3)
    return 5
y = a()
print(y) # 10 -> correct
