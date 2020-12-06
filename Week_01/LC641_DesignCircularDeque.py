class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.queue = []
        self.size = k

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if not self.isFull():
            self.queue.insert(0, value)
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if not self.isFull():
            self.queue.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if not self.isEmpty():
            self.queue.pop(0)
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if not self.isEmpty():
            self.queue.pop()
            return True
        else:
            return False

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if not self.isEmpty():
            return self.queue[0]
        return -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if not self.isEmpty():
            return self.queue[-1]
        return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return 0 == len(self.queue)

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.size == len(self.queue)

