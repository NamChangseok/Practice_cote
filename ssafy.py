import sys

sys.stdin=open('input.txt')
T=int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    num=list(map(int, input().split()))
    #result = sum([j for j in num if j % 2 !=0])
    result=0
    for i in num:
        if i%2!=0:
            result+=i
    print(f"#{test_case}",result)
    # ///////////////////////////////////////////////////////////////////////////////////

    """
    for i in range(1, T + 1):
    
    num = list(map(int, input().split()))

    result = sum([j for j in num if j % 2 != 0])

    print(f"#{i}", result)
    """