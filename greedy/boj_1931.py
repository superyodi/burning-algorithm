

N = int(input())

meeting = []
starts = set()
for _ in range(N):
    s, e = map(int, input().split())

    meeting.append((s, e))
meeting = sorted(meeting, key= lambda x : (x[1], x[0]))

start = meeting[0][0]
count = 0

for time in meeting:
    if time[0] >= start:
        count += 1
        start = time[1]


print(count)