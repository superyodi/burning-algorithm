# Way1. dictionary way

from collections import defaultdict

def solution(n, results):
    answer = 0

    winners = defaultdict(set)
    losers = defaultdict(set)

    for winner, loser in results:
        winners[winner].add(loser)
        losers[loser].add(winner)

    print(winners)
    print(losers)
    for i in range(n):
        player = i + 1
        # 합집합
        for loser in winners[player]:
            winners[player] = winners[player].union(winners[loser])

        for winner in losers[player]:
            losers[player] = losers[player].union(losers[winner])


    for i in range(1, n+1):
       if len(losers[i]) + len(winners[i]) == n-1:
           answer += 1
       else:
           print("딱 맞음", i)

    print(winners)
    print(losers)

    return answer


print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
