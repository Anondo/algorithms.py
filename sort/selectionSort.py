def getMin(x , j):
    mini = x[j]
    for i in range(j , len(x)):
        if(mini > x[i]):
            mini = x[i]
    return mini
def swap(x , i , j):
    temp = x[i]
    x[i] = x[j]
    x[j] = temp
    return x

def selection_Sort(x):
    min = 0
    for i in range(0 , len(x)-1):
        min  = getMin(x , i+1)
        if(x[i] > min):
            x = swap(x , i , x.index(min))
    return x

data = [10 , 14 , 27 , 33 , 35 , 19 , 42 , 44]
data = selection_Sort(data)
print data
