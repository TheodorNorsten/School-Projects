
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// skapar en structur(Klass) för den dubbellänkade listan
struct Node{
  char name[30];
  int data;
  struct Node *prev; // pekare till tidigare nod i listan
  struct Node *next; // pekare till nästa nod i listan

};
/*Skapar en ny nod och returnerar pekare till ny nod.
IN: tal:data sträng:namn attributen till ny nod.
UT: pekare till structurn för den nya noden.
*/
struct Node *skapanod(int ny_data, char nytt_namn[30]){
  struct Node* ny_nod= malloc(sizeof(struct Node));
  ny_nod->data=ny_data;
  strcpy(ny_nod->name,nytt_namn);
  ny_nod->next=NULL;
  ny_nod->prev=NULL;
  return ny_nod;
};

/* lägger till ny nod först i listan
  in: referense(pekare till pekare) till head i listan, pekare till ny nod.
  ut: inget
  */
void push_first(struct Node **head_ref,struct Node* nod){

nod->next = (*head_ref);
// om listan är tom
if((*head_ref)!=NULL){
  (*head_ref)->prev=nod;
};
(*head_ref)=nod;

};

/* Lägger till ny nod efter en given nod(prev) i listan
in: prev_node, noden som ny_nod läggs in framför, pekare för nynod.
ut: inget
*/
void insertAfter(struct Node *prev_node, struct Node* nod){
if(prev_node== NULL){
  printf("input noden är noll, ej tillåtet värde");
  return;
}
// Ändrar om pekarna för noden framför och innan.
nod->next=prev_node->next;
nod->prev=prev_node;

prev_node->next=nod;

if(nod->next!=NULL){
  nod->next->prev=nod;

}

};

/*Lägger till ny nod före nod.
IN: pekare till pekare för head, pekare till nästa nod, pekare till nynod.
UT: inget
*/
void insertBefore(struct Node **head_ref,struct Node *next_node, struct Node* nod){

  if(next_node==NULL){
    printf("Input nod är Noll, ej tillåtet värde");
    return;
  }
nod->next= next_node;

if(next_node->prev ==NULL){
  next_node->prev=nod;
  nod->prev=NULL;
  *head_ref=nod;
  return;
}
next_node->prev->next=nod;
nod->prev= next_node->prev;
next_node->prev=nod;

};


/* Lägger till nod sist i listan.
  IN: referense till första noden i listan(pekar till pekare) och pekare till nynod
  UT: inget
  */

void addera_sist(struct Node **head_ref, struct Node* nod){

struct Node * last= *head_ref;

// om listan är tom.
  if(*head_ref==NULL){
    *head_ref=nod;
    nod->prev=NULL;
    return;
  }
// Traversera genom listan tills sista noden.
while(last->next!=NULL){
  last=last->next;
}
last->next=nod;
nod->prev=last;

return;

};

/* tar bort nod ur listan
IN: pekare till pekare för head och pekare till nod som ska tas bort.
UT:
*/
void tabortnod(struct Node **head_ref,struct Node* nod){
  // bas fall
  if(*head_ref==NULL || nod==NULL){
    printf("Listan är tom");
    return;
  }

  //om noden är headen
  if(*head_ref==nod){
    nod->next->prev=NULL;
    *head_ref=nod->next;
    free(nod);
    return;

  }
  // om noden är sist
  else if(nod->next==NULL){
    nod->prev->next=NULL;
    free(nod);
    return;
  }
  else{
    nod->prev->next=nod->next;
    nod->next->prev=nod->prev;
    free(nod);
    return;

  }

};

/* söker efter nod i listan och returnerar den.
IN: pekare till första elementet i listan, tal:data-värdet för sökt nod.
UT: returnerar pekare till noden om den finns i listan annars sträng.
*/
struct Node *search(struct Node *head_ref,int data){
  while(head_ref!=NULL){
    if (head_ref->data==data){
      return head_ref;
    }
    head_ref=head_ref->next;

  }
  printf("Angiven nod finns inte i listan");
};

/*Skriver ut noden som är inparameter.
IN: pekare till första elementet i listan och pekare till nod som ska skrivas ut.
UT: inget
*/
void printnod(struct Node *head_ref,struct Node* nod){
  while(head_ref!=NULL){
    if(head_ref->name==nod->name){
      printf("{Namn: %s ",nod->name);
      printf("Data: %d}\n", nod->data);
      return;
    }
    head_ref=head_ref->next;
  }
  printf("Angiven Nod finns inte i listan");
};


/* skriver ut alla noder som finns i Listan
IN: pekare till första elementet(head) i noden
UT: inget.
*/
void printlist(struct Node *head_ref){
  /*struct Node *last;*/
  while (head_ref!=NULL) {
    printf("{Namn: %s  ",head_ref->name );
    printf("Data: %d}\n ",head_ref->data);
    /*last=head_ref;*/
    head_ref=head_ref->next;
  }
  printf("\n");
};
