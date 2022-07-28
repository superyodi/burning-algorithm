# Try 1. 우선순위 큐로 해결 


import heapq

def solution(number, k):
    answer = []
    check = [False for _ in range(len(number))]
    cnt = 0
    
    heap = []
    heapq.heappush(heap, (number[0], 0)) # number, index
    
    for i in range(1, len(number)):
        
        while cnt < k and heap:
            num, idx = heapq.heappop(heap)
            
            if num >= number[i]:
                heapq.heappush(heap, (num, idx))
                break
            check[idx] = True
            cnt += 1
        heapq.heappush(heap, (number[i], i))

    if cnt == 0:
        check[-k:] = [True for _ in range(k)]

    for i in range(len(number)):
        if not check[i]:
            answer.append(number[i])
        
    return str(int("".join(answer)))
  
  
 # Try 2. 스택으로 해결 

def solution(number, k):
    answer = ''
    stack = [number[0]]
    
    for num in number[1:]:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)

    if k > 0:
        stack = stack[:-k]

    return str(int(''.join(stack)))
