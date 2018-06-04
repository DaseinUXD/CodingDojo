# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output
# new_list = ['hello','world']


def makeList(wrdList, newChar):
    for i in range(0, len(word_list), 1):
        temp = word_list[i]
        if word_list[i].count(char) > 0 :
            print temp
        idx = wrdList.count(char)
makeList(word_list, char)
