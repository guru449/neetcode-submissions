class DLL:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = self.prev = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.hm = {}
        self.capacity = capacity
        self.left = DLL(0, 0)
        self.right = DLL(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        

    def addToRight(self, node):
        last = self.right.prev
        last.next = node
        node.prev = last
        node.next = self.right
        self.right.prev = node


    def removeFromList(self, node):
        pre = node.prev
        nex = node.next
        pre.next = nex
        nex.prev = pre

    
    def get(self, key: int) -> int:
        if key not in self.hm:
            return -1
        node = self.hm[key]
        self.removeFromList(node)
        self.addToRight(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            node = self.hm[key]
            self.removeFromList(node)
            node.value = value
            self.addToRight(node)
        else:
            node = DLL(key, value)
            self.hm[key] = node
            self.addToRight(node)
        if len(self.hm) > self.capacity:
            lru = self.left.next
            self.removeFromList(self.left.next)
            del self.hm[lru.key]


    


            

        


        
