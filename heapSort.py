def heapify(unsorted,index,heap_size):
    largest = index
    left_index = 2*index+1
    right_index = 2*index+2
    if left_index < heap_size and unsorted[largest]<unsorted[left_index]:
        largest = left_index
    if right_index < heap_size and unsorted[largest] < unsorted[right_index]:
        largest = right_index
    if largest != index:
        unsorted[index],unsorted[largest] = unsorted[largest],unsorted[index]
        heapify(unsorted,largest,heap_size)
def heapSort(unsorted):
    length = len(unsorted)
    for i in range(length//2,-1,-1):
        heapify(unsorted,i,length)
    for i in range(length-1,0,-1):
        unsorted[0],unsorted[i] = unsorted[i],unsorted[0]
        heapify(unsorted,0,i)
    return unsorted

if __name__ == "__main__":
    import argparse
    parse = argparse.ArgumentParser()
    parser.add_argument('integers',nargs='+',type = int,help="some number to sort")
    args = vars(parser.parse_args())
    queue = args['integers']
    print(heapSort(queue))
