# [Try1. Accepted]	392 ms	39.5 MB	python3

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [-1] * (10 ** 6 + 1)

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.arr[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        return self.arr[key]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.arr[key] = -1

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


'''
0 <= key, value <= 106 여서 self.arr = [-1] * (10 ** 6 + 1) 이렇게 초기화하고
bucket 처럼 1:1로 착착 담았다.

하지만 공간낭비가 심해서 다른 방법을 생각해 봐야한다. 

'''

