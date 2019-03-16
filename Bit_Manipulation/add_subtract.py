'''
Add & Subtract Without Plus and Minus: Write a function that adds/subtracts two numbers. You should not use +/-/any arithmetic operators.
'''

def add(a, b):
    while(b != 0):
        summation = a ^ b
        carry = (a & b) << 1
        a = summation
        b = carry
    return a

def subtract(a, b):
    b = ~b
    neg_b = add(b,1)
    if(a>0 and b<0):
        return(add(neg_b,a))
    else:
        return(add(a,neg_b))

if __name__ == '__main__':
    print(add(-2,3))
    #print(subtract(3,2))
