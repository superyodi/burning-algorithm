def solution(n, t, m, timetable):
    timetable.sort()
    lines = {i + 1: [] for i in range(n)}

    hour, minute = 9, 0
    bus = 1

    for time in timetable:
        h_, m_ = map(int, time.split(':'))

        while h_ > hour or (h_ == hour and m_ > minute):
            bus += 1
            if bus > n:
                break
            minute += t
            while minute >= 60:
                hour += 1
                minute -= 60

        if bus > n:
            break

        if len(lines[bus]) < m:
            lines[bus].append((h_, m_))
            continue

        while bus <= n and len(lines[bus]) >= m:

            bus += 1
            minute += t

            while minute >= 60:
                hour += 1
                minute -= 60

        if bus > n:
            break

        lines[bus].append((h_, m_))

    while bus < n:
        bus += 1
        if bus > n:
            break
        minute += t
        while minute >= 60:
            hour += 1
            minute -= 60

    # print(hour, minute)
    # print(lines)

    if len(lines[n]) >= m:
        hour, minute = lines[n][-1]
        minute -= 1

        if minute < 0:
            minute = 59
            hour -= 1

    if hour < 10:
        hour = "0" + str(hour)
    else:
        hour = str(hour)

    if minute < 10:
        minute = "0" + str(minute)
    else:
        minute = str(minute)

    return hour + ":" + minute