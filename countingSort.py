def countingSort(L):
    if L == []:return L
    length = len(L)
    lMax = max(L)
    lMin = min(L)
    counting_arr_length = lMax+1-lMin
    counting_arr = [0]*counting_arr_length
    for number in L:
        counting_arr[number-lMin]+=1
#    for i in range(1,counting_arr_length):
#        counting_arr[i] = counting_arr[i]+counting_arr[i-1]
#
    ordered = [0]*length
    #reversed 用来保证排序算法稳定
   # for i in reversed(range(0,length)):
   #     ordered[counting_arr[L[i]-lMin]-1]=L[i]
   #     counting_arr[L[i]-lMin] -= 1
   # return ordered
    sortedindex=0
    for i in range(counting_arr_length):
        while(counting_arr[i] > 0):
            ordered[sortedindex] = i+lMin
            counting_arr[i]-=1
            sortedindex += 1
    return ordered
if __name__ == "__main__":
    import argparse
    parse = argparse.ArgumentParser()
    parser.add_argument('integers',nargs='+',type = int,help="some number to sort")
    args = vars(parser.parse_args())
    queue = args['integers']
    ordered = countingSort(queue)
    print(ordered)

