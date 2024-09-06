#include <stdio.h>
int main() {
    int a,b,c,n,t;
    printf("no.of.test cases:");
    scanf("%d",&t);
    while(t>0)
    {printf("enter the 1st number:");
     scanf("%d",&a);
     printf("enter the 2nd number:");
     scanf("%d",&b);
     printf("which nth number do you want:");
     scanf("%d",&n);
     while(n>1)
     {  c=a^b;
        a=b;
        b=c;
        n=n-1;
     }
     printf("nth number is %d\n",c);
     t=t-1;
    }
}
