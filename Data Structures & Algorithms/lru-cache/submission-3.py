class LLNode:
    def __init__(self, key, value, nxt, prev):
        self.key = key
        self.value = value
        self.nxt = nxt
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.items = {}
        self.head = LLNode(None, None, None, None)
        self.tail = LLNode(None, None, None, self.head)
        self.head.nxt = self.tail

    def get(self, key: int) -> int:
        if self.size == 0 or (key not in self.items):
            return -1
        
        res = self.items[key].value
        if self.size == 1:
            return res
        # move node to rightmost position
        # start with removing node
        self.remove_node(self.items[key])
        # insert node in rightmost position
        self.insert_right(self.items[key])

        return res
            
    def remove_node(self, llnode):
        prev_node = llnode.prev
        nxt_node = llnode.nxt
        prev_node.nxt = nxt_node
        nxt_node.prev = prev_node

    def insert_right(self, insert_node):
        prev_node = self.tail.prev
        prev_node.nxt = insert_node
        insert_node.prev = prev_node
        insert_node.nxt = self.tail
        self.tail.prev = insert_node

    def put(self, key: int, value: int) -> None:
        if key in self.items:
            self.items[key].value = value
            self.remove_node(self.items[key])
            # insert node in rightmost position
            self.insert_right(self.items[key])
            return
        elif self.size < self.capacity:
            self.size += 1
        else: # cache is full
            del self.items[self.head.nxt.key]
            self.remove_node(self.head.nxt)
            

        self.items[key] = LLNode(key, value, None, None)
        self.insert_right(self.items[key])


        

        
