#include<stdio.h>
#include<stdlib.h>
int main(int argc,char *argv[])
{ int x,y,z,i,j,sum,key,q,p;
  sum=0;
  j=0;
  q=0;
  p=0;
  key=atoi(argv[1]);
  int numbers[9];
  for(y=0;y<10;y=y+1)
  { printf("enter the number:");
    scanf("%d",&numbers[y]);
  }
  y=0;
  for(y=0;y<10;y=y+1)
  { if(key==numbers[y])
    { sum=sum+1;
    }
  }
  printf("%d\n",sum);
    for(i=0;i<10;i=i+1)
     { while(numbers[i]<=numbers[j] && j<10)
       { if(j==9)
         { printf("%d is the minimum of all numbers\n",numbers[i]);
         }
         j=j+1;
       }
     }
      for(q=0;q<10;q=q+1)
    { while(numbers[q]>=numbers[p] && p<10)
      { if(p==9)
        { printf("%d is the maximum of all numbers\n",numbers[q]);
        }
        p=p+1;
      }
    }
    }
 
