#include<stdio.h>
int main()
{ int a,b,c,d,sum,max;
  printf("no of test cases:");
  scanf("%d",&a);
  max=0;
  while(a>0)
  { printf("number of leaves in the pile:");
    scanf("%d",&c);
    while(c>0)
    {printf("magic of the leaf:");
     scanf("%d",&b);
     if(b!=0)
     { sum=sum+b;
     }
     if(b==0 || c==1)
     { if(sum>max)
       { max=sum,sum=0;
       }
     }
     c=c-1;
     if(c==0)
     { printf("%d\n",max);
       max=0;
       sum=0;
     }
    }
    a=a-1;
   }
 }
