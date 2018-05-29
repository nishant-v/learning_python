def print_squ(n):
    newlist = [i*i for i in range(n) if not(i&1==0)]
    return sum(newlist)


num = 4
res = print_squ(num)
print ("{}".format(res))


