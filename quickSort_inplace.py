import math
def quickSort_inplace(L,a,b):
    if b <= a : return
    center = int((a+b)/2)
    if L[a]>L[center]:
        L[center],L[a] = L[a],L[center]
    if L[a]>L[b]:
        L[a],L[b] = L[b],L[a]
    if L[center] > L[b]:
        L[center],L[b] = L[b],L[center]
    pivot = L[center]
    L[center],L[b-1] = L[b-1],L[center]
    left = a
    right = b-2
    while left <= right:
        while L[left]<pivot:
            left+=1
        while L[right]>pivot:
            right -=1
        if left <= right:
            L[left],L[right] = L[right],L[left]
            left,right = left+1,right-1
    L[left],L[b-1]=L[b-1],L[left]
    quickSort_inplace(L,a,left-1)
    quickSort_inplace(L,left+1,b)

if __name__ == "__main__":
    import argparse
    parse = argparse.ArgumentParser()
    parser.add_argument('integers',nargs='+',type = int,help="some number to sort")
    args = vars(parser.parse_args())
    quickSort_inplace(args['integers'],0,len(args['integers'])-1)
    print(args['integers'])


