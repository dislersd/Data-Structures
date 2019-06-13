class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(self.get_size() - 1)

    def delete(self):
        temp = self.storage[0]
        self.storage[0], self.storage[-1] = self.storage[-1], self.storage[0]
        self.storage.pop()
        self._sift_down(0)
        return temp

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        # keep bubbling up until we've reached the top of the heap
        # or we've reached a point where the parent is greater than element
        while index > 0:
            # on a single bubble up iteration:
            # get parent index
            parent = (index - 1) // 2
            # compare our value (child) against value of parent
            # if child value is higher priority that parent:
            if self.storage[index] > self.storage[parent]:
                # swap
                self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
                # update childs index to be new index it is now at
                index = parent
            # otherwise, child is at a valid spot
            # stop bubbling
            else:
                break

    def _sift_down(self, index):
        # grab indices of this elements children and determine which child has larger value
        # if the larger child value is larger than parent value the child element swaps with the parent
        l_child = (2 * index) + 1
        r_child = (2 * index) + 2
        parent = index
        array = self.storage
        if self.get_size() > l_child and array[parent] < array[l_child]:
            parent = l_child
        if self.get_size() > r_child and array[parent] < array[r_child]:
            parent = r_child
        if parent is not index:
            array[index], array[parent] = array[parent], array[index]
            self._sift_down(parent)



heap = Heap()
heap.insert(6)
heap.insert(7)
heap.insert(5)
heap.insert(8)
heap.insert(10)
heap.insert(1)
heap.insert(2)
heap.insert(5)
print(heap.storage)

'''
Notes

We want to be able to access the priority element in O(1) time

1) How can we access something in O(1) time?
    Array indexing
    By Key in a hash table
    By reference (the root of a treee)

2) Insert and Delete: The heap still needs to maintain the priority
    Insertion: What happens when we insert a new priority element?
    Deletion: What happens when we delete the priority element?
        How do we determine the next priority element?


Tree Representation of a Heap

      100
     /   \ 
   19     36
  /  \   /  \ 
 17  3  25   1

 (delete 100)

       36
     /   \ 
   19     25
  /  \      \ 
 17   3      1


 Root is the priority element
 Every child is smaller than parent

 Deletion: Removes the highest priority element
    The children are compared and greater element moves up the heap

Insertion:
    If inserted element is greater than parent swap them else it stays where it is


Array representation of Heap

indexing is super helfpul
prioroty element will be index 0: arr[0]

  0   1    2   3  4  5  6   7  8
[101, 25, 25, 17, 3, 1, 24, 2, 7]

[7, 25, 25, 17, 3, 1, 24, 2]

Deletion:
    Remove 101
    Replace with next highest priority element
    Take very last element(7) in arr and temporarily put it in front arr[0]
    Compare 7 against children(25 and 25)
    Swap larger with smaller (7 -> 25) (25 <- 7)
    Keep swapping until 7 is larger than children

    1. save a reference to the old prio element so we can return it
    2. overwrite the old prio element with the last element in array
    3. remove the last element from array (because we dont want 2 copies of 7)
    4. sift down the element at index 0 (7 )

2(0) + 1 = 1
Left child: 2 * index + 1
Right child: 2 * index + 2
parent: (index - 1) // 2   floor(index minus 1 divided by 2)

Insertion:
    1. Append new element to end of array
    2. Bubble the new element up the heap until it's at a valid spot
    
'''
