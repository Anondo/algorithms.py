lst = [35 , 44 , 42 , 11 , 27 , 14 , 10]
print "The unsorted list: {}".format(lst)
lst.sort()
print "The sorted list: {}".format(lst)
query = int(raw_input("Enter the element to search >>>"))
high = len(lst) - 1
low = 0
mid = (high + low) / 2

while(mid != high and lst[mid] != query):
    if(query < lst[mid]):
        high = mid - 1
        mid = (high + low) / 2
    elif(query > lst[mid]):
        low = mid + 1
        mid = (high + low) / 2
if(lst[mid] == query):
    print "The element {} is in index {} of the list".format(query , lst.index(lst[mid]))
else:
    print "Element not found in list"
