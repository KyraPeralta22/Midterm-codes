def add(val1, val2):
    return val1 + val2 

def sub(val1, val2):
    return val1 - val2

def add(*args):
    return args[0] + args[1] + args[2]

def sub(**kwargs):
    #print (kwargs)
    val1 = kwargs ['val1']
    val2 = kwargs ['val2']
    val3 = kwargs ['val3']

    return val1 - val2 - val3

if __name__ == "__main__":

    sum = add(1, 2)
    # print ("The sum is" + str(sum))
    print (f"The sum is {sum}")

    diff = sub(1, 2)
    # print ("The difference is" + str(diff))
    print (f"The difference is {diff}")

    sum = add(1,2,3)
    print (f"The sum is {sum}")

    diff = sub (val1=1, val2=2, val3=3)
    print (f"The difference is {diff}")

