#include<stdio.h>
#include<math.h>
void cone();
void sphere();
void cuboid();
int main()
{ cuboid();
  cone();
  sphere();
}
void cuboid()
{ int area3,perimiter3,volume3,a;
  printf("enter the side value of cuboid:");
  scanf("%d",&a);
  area3=6*a*a;
  perimiter3=12*a;
  volume3=a*a*a;
  printf("%d is the area of cuboid\n",area3);
  printf("%d is the perimiter of cuboid\n",perimiter3);
  printf("%d is the volume of cuboid\n",volume3);
}
 void cone()
 { int area1,perimiter,volume1,r,h,p;
   printf("enter the value of radius of cone:");
   scanf("%d",&r);
   printf("enter the value of height of cone:");
   scanf("%d",&h);
   p=sqrt((h*h+r*r));
   area1=3.14*r*(r+p);
   volume1=(0.34)*(3.14)*r*r*h;
   printf("%d is the area of cone\n",area1);
   printf("%d is the volume of cone\n",volume1);
   printf("cone has no perimiter\n");
}
void sphere()
{ int area2,perimiter2,volume2,w;
  printf("enter the value of radius of sphere:");
  scanf("%d",&w);
  area2=4*3.14*w*w;
  volume2=1.33*3.14*w*w*w;
  printf("%d is the surface area of sphere\n",area2);
  printf("%d is the volume of sphere\n",volume2);
  printf("sphere has no perimiter\n");
}

