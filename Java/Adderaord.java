import java.util.Scanner;
import java.util.Arrays;
import java.util.ArrayList;

public class Adderaord{
  public static void main(String[] args) {

    Scanner input= new Scanner(System.in);
    boolean bo= true;
    int storlek=0;

    while(bo){
      /*System.out.println("skriv antalet strängar som ska skrivas ut");*/
      try{
          String check= input.next();
          storlek =Integer.parseInt(check);
      }
      catch(Exception e){
        System.out.println("input måste vara en siffra,försök igen\n ");
        continue;
      }

      if(storlek<2 ||storlek>10000){
        System.out.println("Antalet strängar måste vara mellan 2 och 10000, försök igen\n");
        continue;
      }
      else{
        break;}

    }
    String tot="";

    /*System.out.println("Skriv vilka ord som ska skrivas ut");*/
    String[] stringVek= new String[storlek];
    for(int i=0; i<stringVek.length;i++){
      stringVek[i]=input.next();
    }

    for(String i:stringVek){
      tot+=i;
    }
    System.out.println("\n"+ tot);





  }
}
