import collections

def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += hash(part)
    for c in completion:
        temp -= hash(c)
    return dic[temp]