import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.chidren = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert_and_search(self, key):
        now = self.root
        flag = len(key)

        # insert
        for k in key:
            if k not in now.chidren:
                now.chidren[k] = Node(k)
                flag -= 1
            now = now.chidren[k]

            if now.isEndOfWord:
                return True

        now.isEndOfWord = True

        if flag == len(key):
            return True
        return False


N = int(sys.stdin.readline())


for i in range(N):
    trie = Trie()
    M = int(sys.stdin.readline())
    phone_book = []

    isPrefix = False

    for j in range(M):
        s = sys.stdin.readline()[:-1]
        phone_book.append(s)

    for number in phone_book:
        isPrefix = trie.insert_and_search(number)

        if isPrefix:
            print("NO")
            isPrefix = True
            break

    else:
        print("YES")


'''
2
3
123
456
789
5
12
123
1235
567
88


'''


# 반례
# 클래스 변수는 꼭 __init__으로 초기화하자!!!
'''
2
3
12
13
14
2
123
14


'''