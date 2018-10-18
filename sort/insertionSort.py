lst = [35 , 44 , 42 , 27 , 10 , 14]
print "The unsorted list: {}".format(lst)

for i in range(0 , len(lst) - 1):
    if(lst[i] > lst[i+1]):
        lst.insert(i + 1 , lst.pop(i))
    if(i > 0):
        for j in range(0 , lst.index(lst[i])):
            if(lst[i] < lst[j]):
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp

print "The sorted list: {}".format(lst)
