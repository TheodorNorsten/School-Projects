#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "hashfunc.c"

int main(int argc, char * argv[]) {

  my_hash *hashtabell= skapa_hashtabell();



  put(hashtabell,"name1","em");
  put(hashtabell,"name2","russian");
  put(hashtabell,"name3","pizza");
  put(hashtabell,"name4","doge");
  put(hashtabell,"name5","pyro");
  put(hashtabell,"name6","joost");
  put(hashtabell,"name7","kalix");

  printf("%d\n",tilpro_hash("hej"));

printlist(hashtabell);







return 0;

}
