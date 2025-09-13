def solution(sizes):
    answer = 0
    
    first = 0
    second = 0
    for size in sizes:
        if size[0] > size[1]:
            if second < size[1]:
                second = size[1]
            if first < size[0]:
                first = size[0]
        else:
            if second < size[0]:
                second = size[0]
            if first < size[1]:
                first = size[1]
    
    print(first, second)
    answer = first * second
    return answer