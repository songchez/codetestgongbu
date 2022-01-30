# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 
# 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.
# 뒤에있는게 앞에있는거에 존재하는지 확인하는 문제 -이분탐색((Binary Search):중간값과 비교해서 빨리찾기,퀵정렬은 피봇을 기준으로 왼쪽오른쪽으로 옮김,자료형(집합) 

#내풀이 - 시간초과
num_that = int(input())
that = list(map(int,input().split()))
num_to_find = int(input())
to_find = list(map(int,input().split()))
fin_bol = 0 #있는지 없는지 확인할 변수
that.sort()
to_find.sort()
def find_int(that, to_find):
    for x in to_find:
        for i in that: #찾았을때 멈추고 해당숫자 리스트에서 지움(속도 올리기위해), 마지막 fin_bol값을 리턴
            if i == x:
                that.remove(x)
                fin_bol = 1
                break
            elif i != x:
                fin_bol = 0
        print(fin_bol)
find_int(that, to_find)


#다른사람풀이 - 집합자료형(set)을 이용한 알고리즘
from sys import stdin, stdout
num_that = stdin.readline()
that = set(stdin.readline().split())
num_to_find = stdin.readline()
to_find = stdin.readline().split()

for l in to_find:
    stdout.write('1\n') if l in that else stdout.write('0\n')