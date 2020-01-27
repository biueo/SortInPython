def selectSort(L):
    l = len(L)
    if l <=1:return L
    minvalue = None
    for i in range(l):
        minvalue = L[i]
        minindex = i
        for j in range(i,l):
            if L[j]< minvalue:
                minvalue = L[j]
                minindex = j
        L[i],L[minindex] = L[minindex],L[i]
    return L

if __name__ == "__main__":
    import argparse
    parse = argparse.ArgumentParser()
    parser.add_argument('integers',nargs='+',type = int,help="some number to sort")
    args = vars(parser.parse_args())
    print(selectSort(args['integers']))
