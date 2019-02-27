count = 0
def findWays(n):
    if(n == 0):
        print(1)
        return
    global count, unique
    #Store bits starting from LSB to MSB in simple binary format
    positions = []
    copy = n
    while(n>=1):
        positions.append(n%2)
        n = n/2
    helper(positions[:], 0, [0,1,2], copy, 0)   #This will generate all possible combinations
    print(count)

def helper(positions, index, options, n, cur_value):
    if(len(positions) == index+1):    #If you are at the last bit(MSB), then simple try all it's combination
        global count
        for i in options:
            positions[index] = i
            cur_value_copy = cur_value+(2**index)*positions[index]
            if(cur_value_copy > n):                   #Early Stopping as value till now exceeds n
                break
            if(cur_value_copy == n):    #If new value is same as n or not
                count = count + 1
    else:
        #Trying all options for the corresponding bits
        for i in options:
            copy = positions[:]
            copy[index] = i
            cur_value_copy = cur_value+(2**index)*copy[index]
            if(cur_value_copy>n):    #Early Stopping as value till now exceeds n
                break
            helper(copy, index+1, [0,1,2], n, cur_value_copy)

if __name__ == '__main__':
    findWays(10)
