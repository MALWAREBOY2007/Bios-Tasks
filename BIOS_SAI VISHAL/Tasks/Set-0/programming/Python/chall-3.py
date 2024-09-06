n=int(input("no of lines you want:"))
f=1
for i in range (n,0,-1):
    for w in range (0,i,1):
        print(" ",end="")
        if w==i-1:
           j=f
           while j>=0 and j<=n:
              j=j-1
              if j==0:
                  print("*\n")
                  f=f+1
              if j>=1:
                  print("* ",end="")
