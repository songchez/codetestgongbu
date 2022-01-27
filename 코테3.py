def solution(answers):
    supo = {1:[1, 2, 3, 4, 5],
        2:[2, 1, 2, 3, 2, 4, 5],
        3:[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]}
    point = {1:0, 2:0 ,3:0}
    for v in supo.keys():
        for indx, i in enumerate(answers):
            if i == supo[v][indx%len(supo[v])]:
                point[v] +=1
    answer = [k for k,v in point.items() if max(point.values()) == v]
    return answer

print(solution([1,3,2,4,2]))