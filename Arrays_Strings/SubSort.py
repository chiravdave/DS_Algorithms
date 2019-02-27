''' 
Sub Sort: Given an array of integers, write a method to find indices m and n such that if you sorted elements m through n , the entire array would be sorted. 
          Minimize n - m (that is, find the smallest such sequence). 
Input: 1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19
Output: (3, 9) 
'''

def getMaxMin(a, start, end):
    maximum = a[start]
    minimum = a[start]
    start = start + 1
    while(start <= end):
        if(a[start] > maximum):
            maximum = a[start]
        if(a[start] < minimum):
            minimum = a[start]
        start = start + 1
    return maximum, minimum

def subSort(a):
    length = len(a)
    left_end = 0       #Storing end index of the left sorted part
    right_start = length-1  #Storing start index of the right sorted part
    while(left_end < (length-1)):
        if(a[left_end] > a[left_end+1]):
            break
        left_end = left_end + 1
    #list is already sorted
    if(left_end == (length-1)):
        return((-1,-1))
    while(right_start > left_end):
        if(a[right_start] < a[right_start-1]):
            break
        right_start = right_start - 1
    #Get max and min from the middle part of the array
    maximum = a[left_end]
    minimum = a[right_start]
    if(left_end != (right_start-1)):
        mid_max, mid_min = getMaxMin(a, left_end+1, right_start-1)
        maximum = max(maximum, mid_max)
        minimum = min(minimum, mid_min)
    start_index = 0
    end_index = right_start
    #Finding starting index
    while(a[start_index] <= minimum):
        start_index = start_index + 1
    #Finding end index
    while(end_index < length and a[end_index] < maximum):
        end_index = end_index + 1
    return start_index, end_index-1
    
if __name__ == '__main__':
    print('The unsorted range is : {}'.format(subSort([7,6,5])))
