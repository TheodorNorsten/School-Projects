
#include <stdio.h>
#include<string.h>

struct Dog{
  char name[30];
  int age;
  char type[30];

};
/*void skrivutbok(struct Dog* hund);*/

int main(int argc, char *argv[])
{
struct Dog objekt;
struct Dog* hund1;
hund1=&objekt;

hund1->age=5;
strcpy(hund1->name,"lillis");
strcpy(hund1->type,"lab");
printf("%d\n",hund1->age );
printf("%d\n",objekt->age );




  return 0;
}
/*
void skrivutbok(struct Dog* hund){
  printf("%s\n",hund->name);
  printf("%s\n",hund->type);
  printf("%d\n",hund->age);
};*/
