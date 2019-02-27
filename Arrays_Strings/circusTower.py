'''
Circus Tower: A circus is designing a tower routine consisting of people standing on top of one another's shoulders. For practical and aesthetic reasons, each person must be both shorter and lighter than the person below him or her. Given the heights and weights of each person in the circus, write a method to compute the largest possible number of people in such a tower
'''

class People:

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

def getLargestNo(peoples):
    length = len(peoples)
    for i in range(length):
        index = i
        for j in range(i+1,length):
            if(peoples[index].weight < peoples[j].weight):
                index = j
            elif((peoples[index].weight == peoples[j].weight) and (peoples[index].height < peoples[j].height)):
                index = j
        if(i != index):
            temp = peoples[i]
            peoples[i] = peoples[j]
            peoples[j] = temp
    memo = {length-1:1}
    largest = 1
    for i in range(length-2,-1,-1):
        max_length = 1
        for j in range(i+1,length):
            if((peoples[i].height > peoples[j].height) and (memo[j]+1 > max_length)):
                max_length = memo[j] + 1
        memo[i] = max_length
        if(max_length > largest):
            largest = max_length
    return largest

if __name__ == '__main__':
    n_people = int(input("Enter how many people"))
    peoples = []
    for i in range(n_people):
        height = int(input("Enter height"))
        weight = int(input("Enter weight"))
        peoples.append(People(height, weight))
    print('Largest Possible No. is: {}'.format(getLargestNo(peoples)))
