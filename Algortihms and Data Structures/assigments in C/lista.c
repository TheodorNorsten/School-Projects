#include "lista.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char * argv[]) {

  struct Node *head= NULL;
  struct Node *nod1= skapanod(1,"nod1");
  struct Node *nod2= skapanod(2,"nod2");
  struct Node *nod3= skapanod(3,"nod3");
  struct Node *nod4= skapanod(4,"nod4");

  addera_sist(&head,nod1);
  addera_sist(&head,nod2);
  addera_sist(&head,nod3);



  printf("lista består av noder med värden\n");
  printlist(head);


/*
  push_first(&head,nod4);
  printf("nu ska nod 4 finnas först i listan\n");
  printlist(head);*/


   struct Node *hittat=search(head,3);
  printf("den sökta noden har värdet %s\n",hittat->name);
  printnod(head,nod1);
/*
  tabortnod(&head,nod2);
  printf("Nu finns följande noder i listan\n" );
  printlist(head);*/


return 0;

}
