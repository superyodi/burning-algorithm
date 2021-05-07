def solution(cacheSize, cities):
    def LRU(city, idx):
        lru_key = min(cache, key=cache.get)
        cache.pop(lru_key)

        return

    def insert(city, idx):
        time = 0
        if city not in cache:
            time = 5

            if len(cache) == cacheSize:
                LRU(city, idx)

        else:
            time = 1

        cache[city] = idx
        return time

    answer = 0
    cache = dict()

    if cacheSize == 0:
        return 5 * len(cities)

    for idx, city in enumerate(cities):
        city = city.lower()
        answer += insert(city, idx)

    return answer