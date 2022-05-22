
import sys

sys.stdin=open('input.txt')
T=int(input())
for i in range(1,T+1):
    num=list(map(int,input().split()))
    if num[0]<num[1]:
        result='<'
    elif num[0]==num[1]:
        result='='
    elif num[0]>num[1]:
        result='>'
    
    print(f"#{i}",result)