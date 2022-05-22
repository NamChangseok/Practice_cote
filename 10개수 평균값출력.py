
import sys

sys.stdin=open('input.txt')
T=int(input())


for i in range(1,T+1):
    num=list(map(int,input().split()))
    avg=sum(num) / 10
    print(f"#{i}",round(avg))
