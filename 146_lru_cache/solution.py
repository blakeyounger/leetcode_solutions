class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        #initialize hashmap
        self.hashmap = {}

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

        self.capacity = capacity

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hashmap:
            self.remove(self.hashmap[key])
            self.insert(self.hashmap[key])
            return self.hashmap[key].val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.hashmap:
            self.remove(self.hashmap[key])
        self.hashmap[key] = Node(key, value)
        self.insert(self.hashmap[key])

        if len(self.hashmap) > self.capacity:
            #remove from the linked list and delete the LRU from the hashmap
            lru = self.left.next
            self.remove(lru)
            del self.hashmap[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
