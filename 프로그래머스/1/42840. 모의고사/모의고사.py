def solution(answers):
    answer = []
    
    h1 = []
    for i in range(len(answers)):
        if i%5==0: h1.append(1)
        if i%5==1: h1.append(2)
        if i%5==2: h1.append(3)
        if i%5==3: h1.append(4)
        if i%5==4: h1.append(5)
    h2 = []
    for j in range(len(answers)):
        if j%2 == 0: h2.append(2)
        if j%8 == 1: h2.append(1)
        if j%8 == 3: h2.append(3)
        if j%8 == 5: h2.append(4)
        if j%8 == 7: h2.append(5)
    
    h3 = []
    for k in range(len(answers)):
        if k%10 == 0: h3.append(3)
        if k%10 == 1: h3.append(3)
        if k%10 == 2: h3.append(1)
        if k%10 == 3: h3.append(1)
        if k%10 == 4: h3.append(2)
        if k%10 == 5: h3.append(2)
        if k%10 == 6: h3.append(4)
        if k%10 == 7: h3.append(4)
        if k%10 == 8: h3.append(5)
        if k%10 == 9: h3.append(5)
    
    h1_score = 0; h2_score = 0; h3_score = 0
    for idx, ans in enumerate(answers):
        if h1[idx] == ans: h1_score += 1
        if h2[idx] == ans: h2_score += 1
        if h3[idx] == ans: h3_score += 1
    
    temp = [h1_score,h2_score, h3_score]
    _max = max(temp)
    answer = [i+1 for i, x in enumerate(temp) if x == _max]
    answer = sorted(answer)
    return answer