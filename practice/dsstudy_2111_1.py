def solution(cacheSize, cities):
    time = 0
    cache = []

    for city in cities:
        city = city.upper()
        if cacheSize == 0:
            time += 5
            continue
        else:
            if city not in cache:
                time += 5
                if len(cache) < cacheSize:
                    cache.append(city)
                else:
                    cache.pop(0)
                    cache.append(city)
            else:
                time += 1
                cache.pop(cache.index(city))
                cache.append(city)

    return time

cacheSize = 2
cities = ["Jeju", "Pangyo", "NewYork", "newyork"]

# cacheSize = 0
# cities = ["Jeju", "Jeju"]

ret = solution(cacheSize, cities)
print(ret)