lst = [35 , 44 ,42 , 27 , 14 , 10]
print "Unsorted list: {}".format(lst)

for i in range(0 , len(lst) ):
    for j in range(0 , len(lst) - i - 1):
        if(lst[j] > lst[j + 1]):
            lst.insert(j + 1 , lst.pop(j))

print "Sorted list: {}".format(lst)
