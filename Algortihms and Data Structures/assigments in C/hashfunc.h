#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// skapar en struktor för den dubbellänkade listan som fungerar som krockhantering.
typedef struct Node{
}Node;

/*Skapar en srtuktur för hashtabellen. En array bestående av listor.
index är en dubbel pekare till den första noden som finns på giet index värde*/
typedef struct {
}my_hash;

/*Funktion som skapar en nod ur klassen(structorn) Node.
IN: nyckel och värde för ny_nod.
UT: ny_nod, pekare till strukturn.
*/
 Node *skapanod( char *key, char *value);

 /*Skapar hashtabell och sätter alla värden till NULL.
 UT: returnerar en tom array(hashtabellen).
 */
 my_hash *skapa_hashtabell(void);

 /*Hashfunktinen som räknar fram ett hashvärde för input sträng(nyckel). returnerar hashvärde.
 IN: sträng.
 UT: hashvärde(int).
 */
 unsigned int tilpro_hash(const char *key);

 /*lägger till nyckel och värde i hashtabellen.
 om nyckeln redan finns. skrivs värdet över.
 IN: hashtabell, nyckel och värde.
 */
 void put( my_hash *hashtable, char *key, char *value);


 /*Söker efter nyckel i hashtabellen om nyckel finns returneras värdet annars NULL.
 IN: hashtabell, nyckel.
 */
 char * get( my_hash *hashtable, char *key);


 /* Funktinen skriver ut hashtabellens listor.
 IN: hashtabellen.
 */
 void printlist(my_hash *hashtable);
