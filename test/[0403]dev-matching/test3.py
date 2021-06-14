def solution(enroll, referral, seller, amount):
    tree = dict()
    tree['-'] = [None, 0]

    for i in range(len(enroll)):
        name, parent = enroll[i], referral[i]
        tree[name] = [parent, 0]

    for i in range(len(seller)):
        node, val = seller[i], amount[i]
        val *= 100

        # Insert
        while node:
            if val == 0:
                break
            yours = val // 10
            val -= yours

            tree[node][1] += val
            val = yours

            node = tree[node][0]

    result = []

    for k, v in tree.items():
        if k != '-':
            result.append(v[1])

    return result

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
         ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
         ["young", "john", "tod", "emily", "mary"],[12, 4, 2, 5, 10]) )

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["sam", "emily", "jaimie", "edward"],[2, 3, 5, 4]))

