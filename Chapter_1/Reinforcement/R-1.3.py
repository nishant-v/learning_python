def minmax(k):
    min = k[0]
    max = k[0]
    for i in range(len(k)):
        if k[i] < min:
            min = k[i]
        if max < k[i]:
            max = k[i]
    return min,max
        
            
num_list = [2,1,4,11,44,3]
min, max = minmax(num_list)

print ("Max ={}, Min = {}".format(min, max))

