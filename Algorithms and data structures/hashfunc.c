#include <stdio.h>
#include <string.h>
#include <stdlib.h>


const int HASHVEKSIZE = 2097152; // 2^21


// skapar en struktor för den dubbellänkade listan som fungerar som krockhantering.
typedef struct Node{
  char *key;
  char *value;
  struct Node *prev; // pekare till tidigare nod i listan
  struct Node *next; // pekare till nästa nod i listan
}Node;


/*Skapar en srtuktur för hashtabellen. En array bestående av listor.
index är en dubbel pekare till den första noden som finns på giet index värde*/
typedef struct {
  Node **index;
}my_hash;



/*Funktion som skapar en nod ur klassen(structorn) Node.
IN: nyckel och värde för ny_nod.
UT: ny_nod, pekare till strukturn.
*/
 Node *skapanod( char *key, char *value){
   Node* ny_nod= malloc(sizeof( Node) * 1);
   ny_nod->key= malloc(strlen(key) + 1);
   ny_nod->value= malloc(strlen(value) + 1);

  strcpy(ny_nod->key,key);
  strcpy(ny_nod->value,value);
  ny_nod->next=NULL;
  ny_nod->prev=NULL;
  return ny_nod;
};


/*Skapar hashtabell och sätter alla värden till NULL.
UT: returnerar en tom array(hashtabellen).
*/
my_hash *skapa_hashtabell(){
  // allokerar plats för hashtabellen
  my_hash *hashtabell= malloc(sizeof(my_hash) * 1);

  // allokerar antalet index till hashtabellen
  hashtabell->index= malloc(sizeof(Node*) *HASHVEKSIZE);

// initerar alla värden i hashtabellen till NULL
for(int i=0; i<HASHVEKSIZE ; i++){
  hashtabell->index[i]=NULL;
}
  return hashtabell;
};


/*Hashfunktionen som räknar fram ett hashvärde för input sträng(nyckel). returnerar hashvärde.
IN: sträng.
UT: hashvärde(int).
*/
unsigned int tilpro_hash(const char *key) {
  unsigned int  hash = 0;
  size_t i = 0;
  while (key[i] != '\0') {
    hash += key[i++];
    hash += hash << 10;
    hash ^= hash >> 6;
  }
  hash += hash << 3;
  hash ^= hash >> 11;
  hash += hash << 13;

  hash = hash & ( HASHVEKSIZE - 1 );
  return hash;
};



/*lägger till nyckel och värde i hashtabellen.
om nyckeln redan finns. skrivs värdet över.
IN: hashtabell, nyckel och värde.
*/

void put( my_hash *hashtable, char *key, char *value){

   unsigned int hash_index= tilpro_hash(key);
   Node *nod= hashtable->index[hash_index];

  // om ingen nod finns vid hashvärdet
  if(nod==NULL){
    hashtable->index[hash_index]=skapanod(key,value);
    return;
  }

  Node *prev_nod;

  // om det finns nod vid hash_index
  while(nod!=NULL){
    if(strcmp(nod->key,key)==0){
      //nyckeln finns redan
      free(nod->value);
      nod->value= malloc(strlen(value) + 1);
      strcpy(nod->value,value);
      return;
  }
    // gå till nästa nod.
    prev_nod= nod;
    nod=prev_nod->next;

  }
  // lägg till ny nod och peka om pekarna
  prev_nod->next= skapanod(key,value);
  prev_nod->next->prev= prev_nod;

};


/*Söker efter nyckel i hashtabellen om nyckel finns returneras värdet annars NULL.
IN: hashtabell, nyckel.
*/

char * get( my_hash *hashtable, char *key){

  unsigned int hash_index= tilpro_hash(key);

  Node *nod= hashtable->index[hash_index];

  // om det ej finns nod på hash_index
  if(nod==NULL){
    printf("Nyckeln finns inte\n");
    return NULL;
  }

// travesera genom listorna
  while(nod!=NULL){
    // om noden med nyckeln finns returnera värdet.
    if(strcmp(nod->key,key)==0){
      return nod->value;
    }
    nod=nod->next;
  }
  printf("Nyckeln finns inte\n");
  return NULL;
};



/* Funktinen skriver ut hashtabellens listor.
IN: hashtabellen.
*/

void printlist(my_hash *hashtable){

  for( int i=0; i<HASHVEKSIZE; i++){
    Node *nod= hashtable->index[i];
    if(nod==NULL){
      continue;
    }
    printf("index[%4d]: ", i );

    for(;;){
      printf("%s=%s ",nod->key, nod->value );
      if(nod->next==NULL){
        break;}
      nod=nod->next;
    }
    printf("\n" );
  }
};
