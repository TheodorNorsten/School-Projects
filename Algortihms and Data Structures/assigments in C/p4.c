
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

const int HASHVEKSIZE = 1048576;



// skapar en struktur för den dubbellänkade listan
struct Node{
  char *key;
  char value[512];
  struct Node *prev; // pekare till tidigare nod i listan
  struct Node *next; // pekare till nästa nod i listan

};


/*Funktionen lägger till en ny nod med nyckel och värde. Räknar ut hashvärde söker
i den dubbellänkade listan efter key om Nod finns ändras värdet om inte läggs till en nynod.
IN: hashtabellen och två strängar
UT: inget*/
void put( struct Node **hashtable, char *key,char *value){

   unsigned int hash_index= tilpro_hash(key);
  // om ingen nod finns vid hashvärdet
  if(*hashtable[hash_index]==NULL){
    struct Node* ny_nod= malloc(sizeof(struct Node));

    strcpy(ny_nod->key,key);
    strcpy(ny_nod->value,value);
    ny_nod->next=NULL;
    ny_nod->prev=NULL;
    *hashtable[hash_index]=ny_nod;
  }
  // om det finns nod vid hash_index
  else{
    while(*hashtable[hash_index]->next!=NULL){
      *hashtable[hash_index]=*hashtable[hash_index]->next;
    }

    struct Node * ny_nod= malloc(sizeof(struct Node));
    strcpy(ny_nod->key,key);
    strcpy(ny_nod->value,value);
    ny_nod->next==NULL;
    *hashtable[hash_index]->next=ny_nod;
    ny_nod->prev=*hashtable[hash_index];
  }


};


/*Söker efter tillhörande value till input key returnerar värdet(str) om nyckeln finns
annars returneras NULL.
IN: hashtabellen och nyckel(str)
UT: värde(str)
*/

char * get(struct Node **hashtable,char *key){

  unsigned int hash_index= tilpro_hash(key);

  while(hashtable[hash_index]!=NULL && hashtable[hash_index]->key !=key){
    hashtable[hash_index]= hashtable[hash_index]->next;
  }
  if (hashtable[hash_index]==NULL){
    printf("nyckeln finns inte");
    return NULL;
  }
 else{
   return hashtable[hash_index]->value;
 }


};



/*itererar genom hashtabellen och sätter alla index till noll.

*/
void init( struct Node **hashtable){

for( int i=0; i<HASHVEKSIZE;i++){
  *hashtable[i]=NULL;
}



};





int main(int argc, char * argv[]) {

  /*struct Node *head= NULL;
  struct Node *nod1= skapanod("nyckel1","värde1");
  struct Node *nod2= skapanod("nyckel2","värde2");
  struct Node *nod3= skapanod("nyckel3","värde3");
  char *pekare;

  addera_sist(&head,nod1);
  addera_sist(&head,nod2);
  addera_sist(&head,nod3);


  printf("lista består av noder med värden\n");
  printlist(head);
  struct Node *hittat=search(head,3);
  printf("den sökta noden har värdet %s\n",hittat->value);
  printnod(head,nod1);*/


struct Node ** myhashvek= malloc(sizeof( struct Node*) * HASHVEKSIZE);
init(myhashvek);
put(myhashvek,"adam","123");
char *s= get(myhashvek,"adam");
printf("Adam->value %s\n",s );


return 0;

}
