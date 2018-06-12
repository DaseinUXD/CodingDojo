#  1 GIVEN...
x = [ [5,2,3], [10,8,9] ]
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Change the value 10 in x to 15?

x[1][0] = 15 # selected value of x index 1, 0 and set it to 15

print(x) #test work

# change last_name of the first student from Jordan to Bryant

students[0]['last_name'] = 'Bryant'

print (students)

sports_directory['soccer'][0] = 'Andres'

print (sports_directory)

z[0]['y'] = 30

print (z)

# 2. Create a function that given a list of dictionaries, it loops through each dictionary in the list and prints each
# key and the associated value.

students1 = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDict():
    for s in students1:
        print(s)

iterateDict()

# 3. Create a function that given a list of dictionaries and a key name, it outputs the value stored in that key for each dictionary.
# This one still doesn't work correctly although the answer is correct

def iterateDict2():
    for s in students1:

        print(s['first_name'])

iterateDict2()

# 4. Create a function that prints the name of each location and also how many locations the Dojo currently has.
# Have the function also print the name of each instructor and how many instructors the Dojo currently has.

dojo = {
   'location': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def dojoDetails():
    for d in dojo:

        print (d)


dojoDetails()



# Need to return to this one left it aside to move on
