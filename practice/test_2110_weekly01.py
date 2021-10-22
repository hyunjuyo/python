def getIntPoint(l1, l2):
    den = l1[0] * l2[1] - l1[1] * l2[0]
    if den == 0:
        return None

    x = (l1[1] * l2[2] - l1[2] * l2[1]) / den
    y = (l1[2] * l2[0] - l1[0] * l2[2]) / den
    if x != int(x) or y != int(y):
        return None

    return (int(x), int(y))


def drawMap(pointList):
    xPoints = [item[0] for item in pointList]
    yPoints = [item[1] for item in pointList]

    # width = max(xPoints) - min(xPoints) + 1
    # height = max(yPoints) - min(yPoints) + 1
    # print(width, height)

    mapList = []
    for y in range(max(yPoints), min(yPoints) - 1, -1):
        rowInfo = ""
        for x in range(min(xPoints), max(xPoints) + 1):
            if (x, y) in pointList:
                rowInfo += "*"
            else:
                rowInfo += "."
        mapList.append(rowInfo)

    return mapList


def solution(line):
    answer = []

    pointList = []
    for i in range(len(line) - 1):
        for j in range(len(line) - (i + 1)):
            point = getIntPoint(line[i], line[i + j + 1])
            if point != None and point not in pointList:
                pointList.append(point)
    print(pointList)
    answer = drawMap(pointList)
    print(answer)

    return answer


# https://programmers.co.kr/learn/courses/30/lessons/87377
line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]

solution(line)