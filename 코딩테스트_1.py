#TODO:내풀이
def solution(scores):
    new_list = list(map(list, zip(*scores)))
    print(new_list)
    answer = ''
    count_index = 0
    for abc in new_list:
        index_max = abc.index(max(abc))
        index_min = abc.index(min(abc))
        point = 0
        if (abc.count(min(abc)) == 1) and (index_min == abc.index(abc [count_index])) or ((
            (abc.count(max(abc)) == 1) and (index_max == abc.index(abc [count_index])))):
            del abc [count_index]
            point = sum(abc)/len(abc)
        else:
            point = sum(abc)/len(abc)
        if point >= 90:
            answer += "A"
        elif point >= 80:
            answer += "B"
        elif point >= 70:
            answer += "C"
        elif point >= 50:
            answer += "D"
        else:
            answer += "F"

        count_index += 1
    return answer
scores =  [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
print(solution(scores))

#TODO: 다른사람풀이
#윤용규선생님
solution = lambda scores: "".join(map(lambda m: "FDDCBAA"[max(int(sum(m) / len(m) / 10) - 4, 0)], map(lambda m: (m[0], *m[1]) if min(m[1]) <= m[0] <= max(m[1]) else m[1], ((s[i], s[:i] + s[i+1:]) for i, s in enumerate(zip(*scores))))))
#aeanst 선생님
def solution(scores) :
    avgs=[]
    score=[ [i[j] for i in scores] for j in range(len(scores))]
    for idx,i in enumerate(score) :
        avg=sum(i) ; length=len(i)
        if i[idx] == max(i) or i[idx] == min(i) :
            if i.count(i[idx]) == 1 :
                avg-=i[idx] ; length-=1
        avgs.append(avg/length)
    return "".join([ avg>=90 and "A" or avg>=80 and "B" or avg>=70 and "C" or avg>=50 and "D" or "F" for avg in avgs ])
#또다른사람
from collections import Counter
def solution(scores):   
    answer = ''
    for idx, score in enumerate(list(map(list, zip(*scores)))):
        length = len(score)
        if Counter(score)[score[idx]] == 1 and (max(score) == score[idx] or min(score) == score[idx]):
            del score[idx]
            length -= 1
        grade = sum(score) / length
        if grade >= 90:
            answer += 'A'
        elif grade >= 80:
            answer += 'B'
        elif grade >= 70:
            answer += 'C'
        elif grade >= 50:
            answer += 'D'
        else:
            answer += 'F'
    return answer