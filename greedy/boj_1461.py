# 백준 도서관
import sys

N, M = map(int, sys.stdin.readline().split(' '))
books = list(map(int, sys.stdin.readline().split(' ')))
r_books = []
l_books = []
max_book = 0
for b in books:
    if b < 0:
        l_books.append(b * -1)
        continue
    r_books.append(b)

l_books.sort(reverse=True)
r_books.sort(reverse=True)

has_l_books = len(l_books)
has_r_books = len(r_books)

answer = 0

if has_l_books and has_r_books:
    max_book = max(l_books[0], r_books[0])

    flag = False  # 음수와 양수의 절대값이 같을 경우 표시용
    for i in range(0, len(l_books), M):
        if l_books[i] == max_book and not flag:
            answer += l_books[i]
            flag = True
            continue
        answer += 2 * l_books[i]

    for i in range(0, len(r_books), M):
        if r_books[i] == max_book and not flag:
            answer += r_books[i]
            flag = True
            continue
        answer += 2 * r_books[i]

elif has_r_books:
    max_book = r_books[0]

    for i in range(0, len(r_books), M):
        if r_books[i] == max_book:
            answer += r_books[i]
            continue
        answer += 2 * r_books[i]
else:
    max_book = l_books[0]

    for i in range(0, len(l_books), M):
        if l_books[i] == max_book:
            answer += l_books[i]
            continue
        answer += 2 * l_books[i]


print(answer)