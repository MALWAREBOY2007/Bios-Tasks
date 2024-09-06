list=[]
list1=[]
n=int(input("how many cases:"))
while n>0:
    l=int(input("how many phone numbers:"))
    while l>0:
         k=input("phone number:")
         list.append(k)
         l=l-1
    f=len(list[0])
    k=len(list)
    w=0
    z=1
    while w<k:
        r=len(list[0])
        s=len(list[w])
        if r!=s:
            z=z-1
            break
        w=w+1
    a=0
    b=1
    c=0
    x=k*f
    sum=0
    if z==1:
        while x>0:
            if list[0][a]!=list[b][c]:
                break
            if b==k-1:
                a=a+1
                c=c+1
                b=1
                sum=sum+1
            if a==f-1:
                break
            if b!=k-1:
                b=b+1
            x=x-1
        if sum==0:
           list1.append(-1)
        if sum!=0:
           list1.append(sum)
    n=n-1
    if z==0:
        list1.append(-1)
g=len(list1)
q=0
while q<g:
    print(list1[q])
    q=q+1
