def insertSort(L):
    l = len(L)
    if l <=1: return L 
    for i in range(1,l):
        j = i-1
        temp = L[i]
        while L[j]> temp and j >=0:
            L[j+1]= L[j]
            j-=1
        L[j+1] = temp
    return L

if __name__ == "__main__":
    import argparse
    parse = argparse.ArgumentParser()
    parser.add_argument('integers',nargs='+',type = int,help="some number to sort")
    args = vars(parser.parse_args())
    print(insertSort(args['integers']))

