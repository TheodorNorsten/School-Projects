#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "hashfunc.c"
#include "read.c"


int main(int argc, char * argv[]) {

// skapar min hashtabell.
  my_hash *hashtabell= skapa_hashtabell();

  Artist * artister = malloc(sizeof(Artist) * 1000000);
  int antalartister = readartists("song_artist.txt", artister);

// lägger till alla artiser-titel i hashtabellen.
  for (int i = 0; i < antalartister; i++) {
      put(hashtabell, artister[i].artistname, artister[i].songtitle);
         }
  free(artister);


  char *pekare= get(hashtabell,"Pet Shop Boys");
  printf("%s\n",pekare);




  // Testfall
/*
  put(hashtabell,"name1","testa");
  put(hashtabell,"name2","russin");
  put(hashtabell,"name3","pizza");
  put(hashtabell,"name4","hund");
  put(hashtabell,"name5","java");
  put(hashtabell,"name6","python");
  put(hashtabell,"name7","labb");
*/


//printlist(hashtabell);




return 0;

}
