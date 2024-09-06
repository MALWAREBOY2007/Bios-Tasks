N=int(input("enter the number of dungeons:"))
list=[]
for i in range(0, N):
    l= int(input("type(0 and 1):"))
    list.append(l)
    N=N-1
n=len(list)
sum=0
for i in range(0,n,1):
    if list[i]==1:
        p=0
        sum=sum+1
        while p<=n-1:
              if list[p]==0:
                   list[p]=1
              else:
                   list[p]=0
              p=p+1
print(sum)
