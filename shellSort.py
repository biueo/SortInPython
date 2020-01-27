def shellSort(unsorted):
    gaps = [ 701,301,132,57,23,10,4,1 ]
    for gap in gaps:
        i = gap
        while i < len(unsorted):
            j = i-gap
            temp = unsorted[i]
            while j >= 0 and unsorted[j] > temp:
                    unsorted[j+gap] = unsorted[j]
                    j-=gap
            unsorted[j+gap] = temp
            i+=1

if __name__ == "__main__":
    import argparse
    arg = argparse.ArgumentParser()
    arg.add_argument('integers',metavar='N',type = int,nargs='+',help="some number to sort")
    args =vars(arg.parse_args())
    queue = args['integers']
    shellSort(queue)
    print(queue)

