class Dll:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hm = {}
        self.head = Dll(0, 0)
        self.tail = Dll(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def removeFromList(self, node):
        print(node.value)
        previous = node.prev
        nexxt = node.next
        previous.next = nexxt
        nexxt.prev = previous

    def addToTail(self, node):
        previous = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        node.prev = previous
        previous.next = node

    def get(self, key: int) -> int:
        if key not in self.hm:
            return -1
        node = self.hm.get(key)
        self.removeFromList(node)
        self.addToTail(node)
        return self.hm[key].value
        

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            node = self.hm[key]
            node.value = value
            self.removeFromList(node)
        else:
            node = Dll(key, value)
            self.hm[key] = node
        self.addToTail(node)

        if len(self.hm) > self.capacity:
            lruNode = self.head.next
            removeKey = lruNode.key
            self.removeFromList(self.head.next)
            del self.hm[removeKey]
        
