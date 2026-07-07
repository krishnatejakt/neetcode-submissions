class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        self.left = self.right = Node(-1,-1)
        self.left.nxt, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        if key in self.d:
            node = self.d[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1
    
    def insert(self, node):
        prv, nxt = self.right.prev, self.right
        prv.nxt = nxt.prev = node
        node.prev, node.nxt = prv, self.right
    
    def remove(self, node):
        prv, nxt = node.prev, node.nxt
        prv.nxt, nxt.prev = nxt, prv
        

    def put(self, key: int, value: int) -> None:
        
        new_node = Node(key, value)
        if key in self.d:
            self.remove(self.d[key])
        
        self.insert(new_node)
        self.d[key] = new_node
        
        if len(self.d) > self.capacity:
            lru = self.left.nxt
            self.remove(lru)
            del self.d[lru.key]
        
