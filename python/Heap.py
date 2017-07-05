
class Node:
    def __init__(self, parent, left = None, right = None):
           self.parent = parent
           self.left = left
           self.right = right

class Heap:
    def __init__(self, sourceArray  = None):
        self._container = []
        self._container.append(None)
        if(sourceArray != None and len(sourceArray) > 0):
            self._heapify(sourceArray)

    def getHeap(self):
        return self._container

    def getSize(self):
        return len(self._container)

    def _heapify(self, source):
        #assign
        for i in range(0, len(source)):
            self._container.append(source[i])
        #shift down from n/2 -> 1
        for i in range(len(source)/2, 0, -1):
            self._shift_down(i)


    def insert(self, value):
        if(value == None):return
        self._container.append(value)
        self._shift_up(len(self._container) - 1)



    def _shift_up(self, index):
        #put the last node to the right place up in heap
        arr = self._container
        while(index/2 >= 1):
            if(arr[index/2] < arr[index]):
                self._swap(arr, index, index/2)
                index = index/2
            else:
                break


    def extract(self, index = 1):
        #extract the first node
        self._swap(self._container, 1, len(self._container) - 1)
        result = self._container.pop()
        self._shift_down()
        return result



    def _shift_down(self, index = 1):
        #pass the first node to the right place down in heap
        container = self._container
        child = index * 2
        while(child <= len(container) - 1):
            if(container[child + 1] != None and container[child] < container[child + 1]):
                child = child + 1
            if(container[index] >= container[child]):
                break
            else:
                self._swap(container, index, child)
            index = child
            child = index * 2
        return index

    def _swap(self, array, x, y):
        if (x == y): return
        if (array[x] == array[y]): return
        temp = array[x]
        array[x] = array[y]
        array[y] = temp


arr = [1, 3 ,2, 5, 6]
heap = Heap(arr)
print heap.getHeap()
heap.insert(8)
print heap.getHeap()
heap.extract()
print heap.getHeap()

