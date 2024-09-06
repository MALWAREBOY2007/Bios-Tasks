list=[]
n=int(input("enter the number of elements:"))
while n>0:
    v=int(input("enter the number:"))
    list.append(v)
    n=n-1
list2=list
list1=[]
l=len(list)
j=0
i=0
while i<l:
    while list[i]<=list[j] and j<l:
        if list[i]<=list[j] and j==l-1:
            list1.append(list[i])
            print(list1)
            list.remove(list[i])
            l=len(list)
            j=-1
            i=0
            if l==0:
                break
        j=j+1
    i=i+1
c=int(input("which number do you want to check:"))
p=len(list1)
v=0
g=0
while v<p:
    if c==list1[v]:
        g=g+1
        print(v)
        break
    v=v+1
if g!=1:
    print(-1)
