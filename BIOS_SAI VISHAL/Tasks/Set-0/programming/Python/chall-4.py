def encrypt():
     str=input("write the sentence here(for encrypting):")
     v=len(str)
     a=0
     while(a<v):
         m=str[a:a+1]
         l=ord(m)
         while l==32:
             print(" ",end="")
             a=a+1
             m=str[a:a+1]
             l=ord(m)
         while l==44:
             print(",",end="")
             a=a+1
             m=str[a:a+1]
             l=ord(m)
         m=str[a:a+1]
         if  l>=65 and l<=77:
             l=l+13
             k=chr(l)
             print(k,end="")
         l=ord(m)
         if l>=78 and l<=90:
             l=l-13
             g=chr(l)
             print(g,end="")
         l=ord(m)
         if l>=97 and l<=109:
             l=l+13
             q=chr(l)
             print(q,end="")
         l=ord(m)
         if l>=110 and l<=122:
             l=l-13
             b=chr(l)
             print(b,end="")
         a=a+1
encrypt()
def decrypt():
     str=input("\nwrite the sentence here(for decrypting):")
     v=len(str)
     a=0
     while(a<v):
         m=str[a:a+1]
         l=ord(m)
         while l==32:
             print(" ",end="")
             a=a+1
             m=str[a:a+1]
             l=ord(m)
         while l==44:
             print(",",end="")
             a=a+1
             m=str[a:a+1]
             l=ord(m)
         m=str[a:a+1]
         if  l>=65 and l<=77:
             l=l+13
             k=chr(l)
             print(k,end="")
         l=ord(m)
         if l>=78 and l<=90:
             l=l-13
             g=chr(l)
             print(g,end="")
         l=ord(m)
         if l>=97 and l<=109:
             l=l+13
             q=chr(l)
             print(q,end="")
         l=ord(m)
         if l>=110 and l<=122:
             l=l-13
             b=chr(l)
             print(b,end="")
         a=a+1
decrypt()
