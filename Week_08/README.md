## 位运算
### 基本运算
1. & -> 只有当两位都是1时结果为1，否则为0  
2. | -> 至少有1位是1时结果为1，否则为0
3. ^ -> 两位相同为0，不同为1
4. ~ -> 取反，0变1，1变0
5. << 左移，向左进行移位操作，高位丢弃，低位补 0  
6. 右移 >>，向右进行移位操作，对无符号数，高位补 0，对于有符号数，高位补符号位
### 常用技巧
1. x & -x 取最低位1
2. x & (x - 1) 清零最低位1

## LRU Cache -- hashmap + doubled linkedlist or OrderedDict
```
class DLinkedNode():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None


class LRUCache():
    def _add_node(self, node):
        """
        Always add the new node right after head.
        """
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """
        Remove an existing node from the linked list.
        """
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        """
        Move certain node in between to the head.
        """
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """
        Pop the current tail.
        """
        res = self.tail.prev
        self._remove_node(res)
        return res

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.capacity = capacity
        self.size = 0
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.cache.get(key, None)
        if not node:
            return -1

        self._move_to_head(node)
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node = self.cache.get(key, None)
        if not node:
            new_node = DLinkedNode()
            new_node.key = key
            new_node.value = value

            self.cache[key] = new_node
            self._add_node(new_node)

            self.size += 1
            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1

        else:
            node.value = value
            self._move_to_head(node)

```

## 快排和归并排序
### 快排
```
class Solution:

    def sortIntegers2(self, A):
        self.quickSort(A, 0, len(A)-1)

    def quickSort(self, A, start, end):

        if start >= end:
            return

        left, right = start, end

        pivot = A[(start + end) / 2]

        while left <= right:

            while left <= right and A[left] < pivot:
                left += 1

            while left <= right and A[right] > pivot:
                right -= 1

            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1

        self.quickSort(A, start, right)
        self.quickSort(A, left, end)

```

### 归并排序
```
class Solution:
    """
    @param: A: an integer array
    @return: use quick sort, merge sort, heap sort or any O(nlogn) algorithm
    @example: [3, 2, 1, 4, 5], return [1, 2, 3, 4, 5]
    """

    def sortIntegers2(self, A):
        temp = [0 for _ in range(len(A))]
        self.merge_sort(A, 0, len(A)-1, temp)

    def merge_sort(self, A, start, end, temp):

        if start >= end:
            return

        mid = (start + end) / 2
        self.merge_sort(A, start, mid, temp)
        self.merge_sort(A, mid+1, end, temp)
        self.merge(A, start, mid, end, temp)

    def merge(self, A, start, mid, end, temp):

        left, right = start, mid+1
        index = start

        while left <= mid and right <= end:
            if A[left] < A[right]:
                temp[index] = A[left]
                left += 1
            else:
                temp[index] = A[right]
                right += 1

            index += 1

        while left <= mid:
            temp[index] = A[left]
            left += 1
            index += 1

        while right <= end:
            temp[index] = A[right]
            right += 1
            index += 1

        for index in range(start, end+1):
            A[index] = temp[index]

```
