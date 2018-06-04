class MathDojo(object):
    def __init__(self):

        self.result = 0
        self.list = []
        return

    def add(self, *arguments):
        addTot = 0
        for arg in arguments:
            addTot1 = 0
            if isinstance(arg,list):
                self.list = arg
                print('list found')
                print(self.list)
                for item in self.list:
                    addTot1 = addTot1 + item
                    print(addTot1)
                self.result = self.result + addTot1

            elif isinstance(arg,tuple):
                self.list = arg
                print('tuple found')
                print(self.list)
                for item in self.list:
                    addTot1 = addTot1 + item
                    print(addTot1)
                self.result = self.result + addTot1


            else:
                print('not a list')
                print(arg)
                addTot = arg
                print(addTot)
                self.result = self.result + addTot

                # print(self.result)
        return self

    def subtract(self, *arguments):
        subTot = 0
        for arg in arguments:
            subTot1 = 0
            if isinstance(arg,list):
                self.list = arg
                for item in self.list:
                    subTot1 = subTot1 + item
                    print(subTot1)
                self.result = self.result - subTot1
            else:
                # print(arg)
                subTot = arg
                # print(subTot)
                self.result = self.result - subTot
                # print(self.result)
        return self



md = MathDojo()
md1 = MathDojo()
md2 = MathDojo()
md3 = MathDojo()
md4 = MathDojo()
md5 = MathDojo()
# print('------------ (md)')
# print(md)
# print('------------(md.result)')
# print(md.result)
# print('------------(md.add(2))')
# print(md.add(2))
# print(md.add(2, 5))
# print(md.subtract(3, 2))
# print(md.result)
# print(md.result)
#

# result1 = md.add(2)
# result2 = md.add(2, 5)
# result3 = md.subtract(3, 2)

# print(result1, result2, result3)
# print('passing method a list')
finalResult1 = md1.add(1, [2,4,5], 3).result
finalResult2 = md2.add(2,5).result
finalResult3 = md3.subtract([3,2]).result
# print('list inside MathDojo method chain')
# chaining methods with various parameter
finalResult = md.add(2).add(2,5).subtract(3,2).result
# chaining methods with various parameter, including list types
finalResult4 = md4.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result
# chaining methods with various parameter, including tuple types
finalResult5 = md5.add((1), 3,4).add((3,5,7,8), [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result

print('MathDojo Part I Results: ' + str(finalResult))
print('MathDojo Part II Results: ' + str(finalResult4))
print('MathDojo Part III Results: ' + str(finalResult5))
print('MathDojo Results: Part I = {}, Part II = {}, and Part III = {} '.format(finalResult, finalResult4, finalResult5))

# print(finalResult1, finalResult2, finalResult3, finalResult, finalResult4, finalResult5)
# print(finalResult1)
# print(finalResult2)
# print(finalResult3)
# print(finalResult)
# print(finalResult4)
# print('finalResult5')
# print(finalResult5)

