def merge(l1,l2,S):
    length_S = len(S)
    i,j=0,0
    while i+j<length_S:
        if  j>=len(l2) or (i<len(l1) and l1[i] < l2[j]):
            S[i+j] = l1[i]
            i+=1
        else:
            S[i+j] = l2[j]
            j+=1
def mergeSort(L):
    n = len(L)
    if n<2:return
    mid = n//2
    l1 = L[:mid]
    l2 = L[mid:]
    mergeSort(l1)
    mergeSort(l2)
    merge(l1,l2,L)

if __name__ == "__main__":
    import argparse
    parse = argparse.ArgumentParser()
    parser.add_argument('integers',nargs='+',type = int,help="some number to sort")
    args = vars(parser.parse_args())
    queue = args['integers']
    mergeSort(queue)
    print(queue)
