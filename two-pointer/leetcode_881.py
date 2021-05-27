# [Succeed]

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        if people[0] > limit // 2:
            return len(people)

        f, r = 0, len(people) - 1
        cnt = 0

        while f <= r:
            if people[f] + people[r] <= limit:
                f += 1

            cnt += 1
            r -= 1

        return cnt
