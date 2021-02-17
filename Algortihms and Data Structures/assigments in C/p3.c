
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// skapar en struktur för den dubbellänkade listan
struct Node{
  char name[30];
  int data;
  struct Node *prev; // pekare till tidigare nod i listan
  struct Node *next; // pekare till nästa nod i listan

};
struct Node *skapanod(int ny_data, char nytt_namn[30]){
  struct Node* ny_nod= malloc(sizeof(struct Node));
  ny_nod->data=ny_data;
  strcpy(ny_nod->name,nytt_namn);
  ny_nod->next=NULL;
  ny_nod->prev=NULL;
  return ny_nod;
};

/* lägger till ny nod först i listan
  in: referense(pekare till pekare) till head i listan, tal: ny_data
  ut: inget
  */
void push_first(struct Node **head_ref,struct Node* nod){

(nod)->next = (*head_ref);
// om listan är tom
if((*head_ref)!=NULL){
  (*head_ref)->prev=nod;
};
(*head_ref)=nod;

};



/* Lägger till ny nod efter en given nod(prev) i listan
in: prev_node, noden som ny_nod läggs in framför, ny_data värdet för noden.
ut: inget
*/
void insertAfter(struct Node *prev_node, struct Node* nod){
if(prev_node== NULL){
  printf("input noden är noll, ej tillåtet värde");
  return;
}
// Ändrar om pekarna för noden framför och innan.
(nod)->next=prev_node->next;
(nod)->prev=prev_node;

prev_node->next=nod;

if((nod)->next!=NULL){
  (nod)->next->prev=nod;

}

};

void insertBefore(struct Node **head_ref,struct Node *next_node, struct Node* nod){

  if(next_node==NULL){
    printf("Input nod är Noll, ej tillåtet värde");
    return;
  }
(nod)->next= next_node;

if(next_node->prev ==NULL){
  next_node->prev=nod;
  (nod)->prev=NULL;
  *head_ref=nod;
  return;
}
next_node->prev->next=nod;
(nod)->prev= next_node->prev;
next_node->prev=nod;

};


/* Lägger till nod sist i listan.
  in: referense till första noden i listan(pekar till pekare), int ny_data
  ut: inget
  */

void addera_sist(struct Node **head_ref, struct Node *nod){

struct Node * last= *head_ref;

// om listan är tom.
  if(*head_ref==NULL){
    *head_ref=nod;
    (nod)->prev=NULL;
    return;
  }
// Gå igenm till sista noden
while(last->next!=NULL){
  last=last->next;
}
last->next=nod;
(nod)->prev=last;

return;

};

void tabortnod(struct Node **head_ref,struct Node* nod){
  // bas fall
  if(*head_ref==NULL || nod==NULL){
    printf("Listan är tom");
    return;
  }
  //om noden är headen
  if(*head_ref==nod){
    (nod)->next->prev=NULL;
    *head_ref=(nod)->next;
    free(nod);
    return;

  }
  // om noden är sist
  else if((nod)->next==NULL){
    (nod)->prev->next=NULL;
    free(nod);
    return;
  }
  else{
    (nod)->prev->next=(nod)->next;
    (nod)->next->prev=(nod)->prev;
    free(nod);
    return;

  }

}

struct Node *search(struct Node *head_ref,int data){
  while(head_ref!=NULL){
    if (head_ref->data==data){
      return head_ref;
    }
    head_ref=head_ref->next;

  }
  printf("Angiven nod finns inte i listan");
};


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


int main(int argc, char * argv[]) {

  /*struct Node *head= NULL;
  struct Node *nod1= skapanod(1,"nod1");
  struct Node *nod2= skapanod(2,"nod2");
  struct Node *nod3= skapanod(3,"nod3");


  addera_sist(&head,nod1);
  addera_sist(&head,nod2);
  addera_sist(&head,nod3);


  printf("lista består av noder med värden\n");
  printlist(head);
  struct Node *hittat=search(head,3);
  printf("den sökta noden har värdet %d\n",hittat->data);
  printnod(head,nod1);

  tabortnod(&head,nod2);
  printf("Nu finns följande noder i listan\n" );
  printlist(head);*/

  char str1[]= "hej";
  char str2[]= "hej";
  char str3[]= "dore";
  if(strcmp(str1,str2)==0){
    printf("samma värde\n" );
  }
else{
  printf("olika värde\n" );
}




  //printf("sökt nod har namnet: %s\n",snod->name);
  //printf("sökt nod har datan: %d\n",snod->data);




/*
  insertAfter(head->next,8);
  insertBefore(&head,head->next->next,10);
  printf(" dubbellänkade listan är: ");
  printlist(head);*/



return 0;

}
