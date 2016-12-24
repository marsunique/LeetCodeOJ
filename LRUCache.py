class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.key_dict = {}
        self.key_position = []
        

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.key_dict:
            self.key_position.remove(key)
            self.key_position.insert(0, key)
            return self.key_dict[key]
        return -1
        

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.key_dict:
            self.key_dict[key] = value
            self.key_position.remove(key)
            self.key_position.insert(0, key)
        elif self.capacity == len(self.key_position):
            removed_key = self.key_position.pop()
            del(self.key_dict[removed_key])
            self.key_dict[key] = value
            self.key_position.insert(0,key)
        else:
            self.key_dict[key] = value
            self.key_position.insert(0, key)


# Using dict and double linked list
class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.key_dict = {}
        self.head = Node(-2, -2)
        self.tail = Node(-2, -2)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.key_dict:
            node = self.key_dict[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.key_dict:
            self._remove(self.key_dict[key])
        elif self.capacity == len(self.key_dict):
            node = self.tail.prev
            self._remove(node)
            del(self.key_dict[node.key])
        node = Node(key, value)
        self._add(node)
        self.key_dict[key] = node
    
    def _add(self, node):
        n = self.head.next
        node.next = n
        node.prev = self.head
        n.prev = node
        self.head.next = node

    def _remove(self, node):
        prevone = node.prev
        nextone = node.next
        prevone.next = nextone
        nextone.prev = prevone

test = LRUCache(2)
print test.get(2)
test.set(2,6)
print test.get(1)
test.set(1,5)
test.set(1,2)
print test.get(1)
print test.get(2)