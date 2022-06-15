def solution(prices):
    
    stocks = [[0,prices[0]]]
    answer = [len(prices)-1-i for i in range(len(prices))]

    for i in range(1, len(prices)):
        s = prices[i]
        while stocks:
            pi, ps = stocks[-1]
            if s < ps:
                answer[pi] = i - pi
                stocks.pop()
            else:
                break
        stocks.append((i, s))

    return answer
