def is_even(k):
    if (k&1==0):
        return True
    return False

num = 11
result = is_even(num)
print ("{}".format(result))