# [Try Accepted]	40 ms	16.5 MB


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    max_length = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return -1

            # go down
            left = dfs(node.left)
            right = dfs(node.right)

            self.max_length = max(self.max_length, left + right + 2)
            return max(left, right) + 1

        dfs(root)

        return self.max_length

'''
쉽지않은 문제였다.
트리 안의 가장 길이가 먼 두 노드를 구하는 문제여서 root를 기준으로 left+right 한 값을 계속 업데이트해야 했다.
self.max_length = max(self.max_length, left + right + 2) 이런 방식으로 max_length를 업데이트 했다.

1) self.max_length = max(self.max_length, left + right + 2)

왜 left+right가 아니고 left+right+2 인가? 2를 왜 더해주는가?

경로를 생각해보면 left ---(edge)-----root-----(edge)-----right
이렇게 왼쪽 경로 + 오른쪽 경로를 하면 root와 연결된 edge 두개를 추가해줘야하므로 +2 해준다. 

2) return max(left, right) + 1
root를 기준으로 left와 right를 순회한 다음 return max(left, right)를 해주는게 아니라
1을 더한 값을 하는가??

left(val: 2) ----(edge)---root-----(edge)-----right(val:3)
위에서 right의 값이 3으로 더 커서 right를 채택하려 한다. 여기에 root에서 right로 가는 edge하나도 추가되므로 +1 해줘야한다.




'''

