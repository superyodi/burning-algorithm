# 739. Daily Temperatures



# [Try 1: Time Limit Exceeded]
class Solution1:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        def findWarmer(start):
            now = start
            while start < len(T):
                if T[now] < T[start]:
                    return start - now
                start += 1
            return 0

        answer = []

        for i in range(len(T)):
            answer.append(findWarmer(i))

        # print(answer)
        return answer


# [Try 2: Accepted]	588 ms	20.8 MB
class Solution2:
    def dailyTemperatures(self, T: List[int]) -> List[int]:

        answer = []
        # (idx, val)
        days = []

        for i in range(len(T)):
            now = T[i]

            while days and days[-1][1] < now:
                # print(days)
                day = days.pop()
                answer.append((day[0], i - day[0]))

            days.append((i, now))

        for day in days:
            answer.append((day[0], 0))

        answer = list(map(lambda x: x[1], sorted(answer, key=lambda x: x[0])))

        return answer

# [Try 3: Accepted]	528 ms	19.3 MB
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:

        answer = [0] * len(T)
        # (idx, val)
        days = []

        for i in range(len(T)):
            now = T[i]

            while days and days[-1][1] < now:
                # print(days)
                day = days.pop()
                answer[day[0]] = i - day[0]

            days.append((i, now))

        return answer

'''
Solution2는 
아직 warmer day를 찾지 못한 day 리스트 중에 now 보다 작은 day가 있을때
answer에 (day, warmer day - day) 이런 형식으로 저장했다.
day들은 언제 warmer day를 만나느냐에따라 answer에 저장되는 시기가 달라서
for 문을 돈 이후 x[0]을 기준으로 sort하고 x[1]의 값만 취하도록 했다.

Solution3에서는 
answer = [0] * len(T) 로 초기화하고
answer[day[0]] = i - day[0] 이런식으로 direct access하도록 했다.
이 방법으로 Solution2보다 시간, 공간효율을 현저히 낮출 수 있었다. 


'''


# [Try 4: Accepted]	488 ms	18.8 MB
class Solution4:
    def dailyTemperatures(self, T: List[int]) -> List[int]:

        answer = [0] * len(T)
        # idx 인덱스
        days = []

        for i in range(len(T)):
            now = T[i]

            while days and T[days[-1]] < now:
                # print(days)
                day = days.pop()
                answer[day] = i - day

            days.append(i)

        return answer

'''
Solution3에서 days를 (idx, val) 이렇게 2차월 배열로 저장했다. 
하지만 생각해보니 idx만 알면 T[idx] = val 이므로
굳이 2차원 배열로 저장할 필요가 없었다....
I'm so stupid : (

'''