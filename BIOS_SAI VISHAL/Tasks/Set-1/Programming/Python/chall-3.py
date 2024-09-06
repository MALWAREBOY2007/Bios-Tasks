list1=[]
n=int(input("enter the no of cases:"))
for a in range(0,n,1):
    trees=int(input("no of trees:"))
    k=0
    list=[]
    while k<=trees-1:
        num=int(input("enter the number(0 or 1):"))
        list.append(num)
        k=k+1
    l=len(list)
    p=0
    sum=0
    while p<l:
            if list[p]==0:
               sum=sum+1
               if p==l-1:
                   list1.append(sum)
            if list[p]==1 and p!=0:
               list1.append(sum)
               break
            if list[p]==1 and l==1:
                list1.append(0)
            p=p+1
k=len(list1)
p=0
while p<k:
    print(list1[p])
    p=p+1
