# 2110
def strToList(str):
    ret = []

    tmpList = str.split("},{")
    tmpList[0] = tmpList[0].split("{{")[1]
    tmpList[-1] = tmpList[-1].split("}}")[0]

    for string in tmpList:
        r = string.split(",")
        ret.append(r)

    return ret


def solution(s):
    answer = []
    sList = strToList(s)

    lenInfo = []
    for v in sList:
        lenInfo.append(len(v))

    for length in range(1, len(sList) + 1):
        i = lenInfo.index(length)
        for v in sList[i]:
            if int(v) not in answer:
                answer.append(int(v))

    return answer

# 211112
def toSortedTuple(s):
    tmp = [tuple(map(int, v.split(','))) for v in s[2:-2].split('},{')]
    ss = [0] * len(tmp)
    for v in tmp:
        ss[len(v) - 1] = v

    return ss


def solution(s):
    answer = []
    ss = toSortedTuple(s)

    for v in ss:
        for v1 in v:
            if v1 not in answer:
                answer.append(v1)

    return answer