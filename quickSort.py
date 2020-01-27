def quickSort(L):
    l = len(L)
    if l <= 1: return L
    left = 0
    right = l-1
    pivot = l-1
    left_sublist = []
    right_sublist = []
    for i in range(left,right):
        if L[i] <= L[pivot]:
            left_sublist.append(L[i])
        else:
            right_sublist.append(L[i])
    left_sublist = quickSort(left_sublist)
    right_sublist = quickSort(right_sublist)
    return left_sublist+[L[pivot]]+right_sublist
if __name__ == "__main__":
    import argparse
    parse = argparse.ArgumentParser()
    parser.add_argument('integers',nargs='+',type = int,help="some number to sort")
    args = vars(parser.parse_args())
    print(quickSort(args['integers']))
