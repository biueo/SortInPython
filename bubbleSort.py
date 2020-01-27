def bubbleSort(L):
    l = len(L)
    if l<=1:return L
    j = l - 1
    swap = False
    while j > 0 :
        for i in range(j):
            if L[i] > L[i+1]:
                L[i],L[i+1] = L[i+1],L[i]
                swap = True
        if not swap:
            break
        j-=1
    retrun L

if __name__ == "__main__":
    import argparse
    parse = argparse.ArgumentParser()
    parser.add_argument('integers',nargs='+',type = int,help="some number to sort")
    args = vars(parser.parse_args())
    print(bubbleSort(args['integers'])
