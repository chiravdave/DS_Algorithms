def main(arr, x):
    n_ele = len(arr)
    new_end = partition(arr, 0, n_ele-1, x)
    partition(arr, 0, new_end-1, x-1)
    
def partition(arr, start, end, x):
    while start <= end:

        while start <= end and arr[start] <= x:
            start += 1

        while start <= end and arr[end] > x:
            end -= 1

        if start < end:
            arr[start], arr[end] = arr[end], arr[start]

    return start
            
if __name__ == "__main__":
    arr = [9, 12, 3, 5, 14, 10, 10]
    main(arr, 10)
    print(arr)