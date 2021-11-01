def isInside(nX, nY, rectangle):
    ret = False
    # print("isIn", nX, nY)
    for rec in rectangle:
        if (rec[0] < nX and nX < rec[2]) and (rec[1] < nY and nY < rec[3]):
            ret = True
            break
    # print("isIn", ret)
    return ret


def isOutside(nX, nY, rectangle):
    check = 0
    # print("isOut", nX, nY)
    for rec in rectangle:
        if not ((rec[0] <= nX and nX <= rec[2]) and (rec[1] <= nY and nY <= rec[3])):
            check += 1
    # print("isOut", check, len(rectangle), check == len(rectangle))
    if check == len(rectangle):
        return True
    else:
        return False


def getMoveLen(steps, rectangle, characterX, characterY, itemX, itemY):
    moveLen = 0

    nowX = characterX
    nowY = characterY
    lX = -1
    lY = -1
    # for n in range(5):
    while True:
        for step in steps:
            nX = nowX + step[0]
            nY = nowY + step[1]
            # print(nX, nY)
            if (nX, nY) != (lX, lY) \
                    and isInside(nX - step[0] / 2, nY - step[1] / 2, rectangle) == False \
                    and isOutside(nX - step[0] / 2, nY - step[1] / 2, rectangle) == False:
                lX = nowX
                lY = nowY
                nowX = nX
                nowY = nY
                # print(f'lX:{lX}, lY:{lY}, nowX:{nowX}, nowY:{nowY}')
                moveLen += 1
                break
        if nowX == itemX and nowY == itemY:
            break
    return moveLen


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    moveLen1 = getMoveLen(steps, rectangle, characterX, characterY, itemX, itemY)
    moveLen2 = getMoveLen(steps[::-1], rectangle, characterX, characterY, itemX, itemY)

    answer = min(moveLen1, moveLen2)

    return answer