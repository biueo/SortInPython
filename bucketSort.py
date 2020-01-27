from shellSort import shellSort

def bucketSort(L):
    length = len(L)
    if length<2:return L
    bucketsize = 5
    lMax = max(L)
    lMin = min(L)
    bucketnumber = (lMax-lMin) // bucketsize +1
    buckets=[]
    for i in range(bucketnumber):
        buckets.append([])
    for i in range(length):
        buckets[(L[i]-lMin)//bucketsize].append(L[i])
    ordered = []
    for i in range(bucketnumber):
        shellSort(buckets[i])
        for j in buckets[i] :
            ordered.append(j)
    return ordered
if __name__ == "__main__":
    import argparse
    parse = argparse.ArgumentParser()
    parser.add_argument('integers',nargs='+',type = int,help="some number to sort")
    args = vars(parser.parse_args())
    queue = args['integers']
    print(bucketSort(queue))


