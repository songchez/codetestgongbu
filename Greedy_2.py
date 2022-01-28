
#회의실 계획 짜기
#가장 빨리끝나는 회의를 고르면 된다.(남은시간이 가장 많기 때문)
#meets = [[1,4],[3,5],[0,6],[5,7],[3,8],[5,9],[6,10],[8,11],[8,12],[2,13],[12,14]]

num_meets = int(input())
meets = list()
for i in range(num_meets):
    meets.append(list(map(int, input().split())))

def greedyMeets(meets):
    meets.sort(key=lambda x:x[1])
    selected = [meets[0]]
    for meet in meets:
        if selected[-1][1] <= meet[0]:
            selected.append(meet)
    return len(selected)

print(greedyMeets(meets))



