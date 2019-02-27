'''
RParens: Implement an algorithm to print all valid (i.e., properly opened and closed) combinations of n pairs of parentheses.
'''

def validCombs(open_left, closed_left, curr_str, all_combs):
    if open_left == 0 and closed_left == 0:
        all_combs.append(curr_str)
    else:
        if open_left > 0:
            validCombs(open_left-1, closed_left, curr_str+'(', all_combs)
        if closed_left >0 and closed_left > open_left:
            validCombs(open_left, closed_left-1, curr_str+')', all_combs)

def main():
    pairs = int(input("Enter no of of pairs"))
    all_combs = []
    validCombs(pairs, pairs, '', all_combs)
    print(all_combs) 

if __name__ == "__main__":
    main()
