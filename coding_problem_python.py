#23rd June 2024

#Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.

#For example, given 156, you should return 3.

def max_consecutive_one(integer):
    counter_max = 0 #max number of 1's
    counter_curr = 0 #current number of 1's
    binary = bin(integer)[2:] # convert integer to binary
    for x in binary:
        print(x)
        if (x == "1"):
            counter_curr += 1
        else:
            counter_max = max(counter_max, counter_curr)
            counter_curr = 0
    return(counter_max)

print(max_consecutive_one(156))

