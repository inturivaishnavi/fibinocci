#fibinociseries
n=int(input("enter no of series that you want to print:"))
first=0
second=1
for i in range(n):
    print(first)
    temp=first
    first=second
    second=temp+first
