def compare(list1, list2):
    if len(list1) != len(list2):
        print "The lists are not the same."
        return
    i = 0

    for i in range(0, len(list1) , 1):
        # print i

        if list1[i] != list2[i]:
            print "The lists are not the same."
            # break
        # elif list1[i] == list2[i]:
        #     # print "The lists are the same"
        #     break
        else:
            print "The lists are the same."
            break
list1 =['celery','carrots','bread','milk']
list2= ['celery','carrots','bread','cream']

# list1 = [1,2,5,6,5]
# list2= [1,2,5,6,5,3]
#
# list1 = [1,2,5,6,5,16]
# list2= [1,2,5,6,5]
#
# list1 = [1,2,5,6,2]
# list2 = [1,2,5,6,2]

compare(list1, list2)