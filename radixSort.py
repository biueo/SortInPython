def radixSort(L,maxDigit):
    length = len(L)
    if length <2: return L
    mod = 10
    dev = 1
    counter = []
    for i in range(maxDigit):
        for n in range(10):
            counter.append([])
        for j in range(length):
            bucket = L[j] % mod // dev
            counter[bucket].append(L[j])
        sortedindex = 0
        for j in range(10):
            for n in counter[j]:
                L[sortedindex] = n
                sortedindex += 1
        counter = []
        mod *= 10
        dev *= 10
    return L

if __name__ == "__main__":
    import argparse
    parse = argparse.ArgumentParser()
    parser.add_argument('integers',nargs='+',type = int,help="some number to sort")
    args = vars(parser.parse_args())
    queue = args['integers']
    print(radixSort(queue,3))


