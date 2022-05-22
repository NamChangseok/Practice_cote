import sys

sys.stdin=open('input.txt')
T=int(input())

j=0

for i in range(T):
    date=input()
    year=int(date[:4])
    month=int(date[4:6])
    day=int(date[6:])
    j+=1
    if month<1 or month>12:
        print(f"#{j} -1")
        continue

    if day<1 or day>31:
        print(f"#{j} -1")
        break

    if month ==2:
        if day>28:
            print(f"#{j} -1")
            continue

    if month in [4,6,9,11]:
        if day>30:
            print(f"#{j} -1")
            continue
            
    print(f"#{j} %04d/%02d/%02d" %(year,month,day))
   
