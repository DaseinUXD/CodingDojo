class User(object): #  creates ?class? User inherited form object
    name = "Anna"   #  creates variable/attribute 'name" and sets its value to
                    #  to "Anna"


anna = User() # instantiates a new instance of User
              # 'anna' as a new class of User with
# the characteristics of the parent

print "anna's name: ", anna.name  # prints the requested string and object/class??.attribute
User.name = "Bob" # set the attribute of the parent class to
# the value "Bob" continues to keep the values of attributes of the parent class even when
# the instance has been created before the change in the parent.
                    #
print "anna's name after change:", anna.name
bob = User() # instantiates new instance of User named 'bob'
print "bob's name:", bob.name

# ///////////////////////////////////////////////


class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logged = False
user1 = User("Anna Propas", "anna@anna.com")
print user1.name
print user1.logged
print user1.email
