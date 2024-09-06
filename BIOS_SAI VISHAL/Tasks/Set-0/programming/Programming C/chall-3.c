#include<stdio.h>
int main()
{ int a,b,c,sum;
  char name[1000];
  b=0;
  sum=0;
  printf("type the word:");
  fgets(name,sizeof(name),stdin);
  for(b=0;name[b]!='\0';b=b+1)
  { if(name[b]=='a' || name[b]=='A')
    { sum=sum+1;
    }
    if(name[b]=='e' || name[b]=='E')
    { sum=sum+1;
    }
    if(name[b]=='i' || name[b]=='I')
    {sum=sum+1;
    }
    if(name[b]=='o' || name[b]=='O')
    {sum=sum+1;
    }
    if(name[b]=='u' || name[b]=='U')
    {sum=sum+1;
    }
  }
  printf("%d",sum);
}
  
