from itertools import permutations


def getCount(k, case):
    count = 0
    for v in case:
        if k < v[0]:
            break
        k -= v[1]
        count += 1
    return count


def solution(k, dungeons):
    answer = -1

    cand = []
    cases = permutations(dungeons, len(dungeons))

    for case in cases:
        count = getCount(k, case)
        if count not in cand:
            cand.append(count)

    print(cand)
    answer = max(cand)

    return answer