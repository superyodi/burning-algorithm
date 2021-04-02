# BOJ_13023 ABCDE

def dfs(v, depth):
    print("{}번째 노드 호출됨".format(v))
    global done
    if depth == 4 or done:
        done = True
        return True

    visited[v] = True
    # v에 연결된 자식노드들 u
    for u in graph[v]:
        # 자식노드 이미 발견했으면 다른자식 찾으러가셈
        if visited[u]: continue
        dfs(u, depth+1)

    # 자식노드의 끝까지 판 다음에 다시 올라가게 하기위해서
    visited[v] = False


N, M = map(int, input().split())
graph = [[] for _ in range(N)]
done = False

# 그래프 생성
for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

visited = [False] * N

print(graph)


for v in range(N):
    if not visited[v]:
        dfs(v, 0)
    # 이전 노드에서 이미 1이 나왔을경우를 위한 flag
    if done: break


print("1") if done else print("0")

print(visited)




'''
6 6
0 1
1 2
2 0
3 4
4 5
5 3

=> 0
'''

'''
7 5
0 1
2 3
3 4
4 5
5 6

정답: 1
출력: 0
'''

'''
6 5
1 2
2 4
2 3
3 4
4 5

정답: 1
'''

