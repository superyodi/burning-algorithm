def solution(enroll, referral, seller, amount):
    # name : (parent, total)
    Node  = {"-" : ["x", 0]}

    for i in range(len(enroll)):
        Node[enroll[i]] = [referral[i], 0]

    for i in range(len(seller)):
        income = amount[i] * 100
        child = seller[i]

        while  child in Node:

            parent = Node[child][0]
            yours = income // 10
            mine = income - yours
            Node[child][1] += mine
            income = yours

            child = Node[child][0]

    result = []
    for k, v in Node.items():
        if k != "-":
            result.append(v[1])

    return result

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
         ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
         ["young", "john", "tod", "emily", "mary"],[12, 4, 2, 5, 10]) )

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["sam", "emily", "jaimie", "edward"],[2, 3, 5, 4]))