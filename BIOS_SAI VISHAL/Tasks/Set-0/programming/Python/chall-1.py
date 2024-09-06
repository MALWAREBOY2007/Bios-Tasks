str=input("enter the word here: ")
a=65
l=len(str)
b=l
str1=""
while l>0 and b>=1:
    m=str[b-1:b]
    str1=str1+m
    b=b-1
    l=l-1
print(str1)
while a<=90 or a>=97 :
    if a<=122:
         sum=0
         n=len(str)
         x=chr(a)
         if a==90:
             a=a+7
         else:
             a=a+1
         while n>0:
              p=str[n-1]
              if x==p:
                 sum=sum+1
              n=n-1
         if sum==1:
                print(x,"occured",sum,"time in the string")
         if sum>=2:
                print(x,"occured",sum,"times in the string")

