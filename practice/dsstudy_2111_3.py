from itertools import permutations
import re

def doUpdate(nums, signs, i, calResult):
    nums.pop(i)
    nums[i] = calResult
    signs.pop(i)

def solution(expression):
    answer = 0
    nums = re.findall(r'\d+', expression)
    
    # test = re.split(r'\d+', expression)
    # print("here~!!!", test)

    signs = []
    for c in expression:
        if c in ['*', '+', '-']:
            signs.append(c)
    # print(nums)
    # print(signs)
    
    for signOrder in permutations(set(signs), len(set(signs))):
        nums2 = nums.copy()
        signs2 = signs.copy()
        for sign in signOrder:
            count = signs2.count(sign)
            while count > 0:
                i = signs2.index(sign)
                calStr = f'{nums2[i]}{sign}{nums2[i+1]}'
                calResult = eval(calStr)
                doUpdate(nums2, signs2, i, calResult)
                print(nums2)
                print(signs2)
                count -= 1
        if abs(nums2[0]) > answer:
            answer = abs(nums2[0])

    print("result", answer)
    
    return answer

expression = "100-200*300-500+20"

ret = solution(expression)
print(ret)