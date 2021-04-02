# quick sort 구현

def quick_sort(start, end):
    global n

    if start >= end:
        return

    pivot = n[start]
    # print("pivot:",pivot)
    low = start + 1
    high = end


    while low <= high:
        while low < end + 1 and n[low] <= pivot: low += 1
        while high > start and n[high] > pivot: high -= 1

        if low <= high:
            n[low], n[high] = n[high], n[low]

    if n[high] < pivot:
        n[start], n[high] = n[high], n[start]

    # print(n)
    # print("_pivot",n[high])


    quick_sort(start, high - 1)
    quick_sort(high + 1, end)


T = int(input())
n = []
while T:
    n = list(map(int, input().split()))
    quick_sort(0, len(n) - 1)

    print(n[-3])
    T -= 1


# test code
# n = [1,1,1,1,1,1, 9,4,5,1,2,6,1000,9]
#
# quick_sort(0, len(n) - 1)
#
# print(n)