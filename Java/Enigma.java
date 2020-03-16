import java.util.Scanner;
import java.util.Arrays;
import java.util.ArrayList;

public class Enigma{
  public static void main(String[] args){

    System.out.println("skriv en krypterad text");

    Scanner input= new Scanner(System.in);
    //Läser in input till strängar
    String krypt_text=input.next();
    System.out.println("skriv en klar text");
    String klar_text= input.next();

    // initierar ArrayList
    ArrayList<String> krypt_lista= new ArrayList<String>();
    ArrayList<String> klar_lista= new ArrayList<String>();

    // konverterar input strängar till ArrayList
    for(char i=0; i<krypt_text.length(); i++){
        char c=krypt_text.charAt(i);
        String s= String.valueOf(c);
        krypt_lista.add(s);
    }
    //System.out.println(krypt_lista);

    for(char i=0; i<klar_text.length(); i++){
        char c=klar_text.charAt(i);
        String s= String.valueOf(c);
        klar_lista.add(s);
    }
    //System.out.println(klar_lista);

    // Initerar hjälpvariabler till while loop
    int position=0;
    ArrayList<Integer> utdata_lista=new ArrayList<Integer>();
    boolean found=true;


    // While loop

    while(krypt_lista.size()>=klar_lista.size()){

      position+=1;

      for(int i=0; i<klar_lista.size(); i++){
        // kontrollerar om elementen är lika i listorna
        if(klar_lista.get(i).equals(krypt_lista.get(i))){
          found=false;
          break;}

        else{
          found=true;
          continue;}
      }

      // ute ur for loop
      // Antingen har vi breakat eller så har vi gått igenom alla element i klar_text
      // Kolla om boolean är true eller inte för att avgöra anledning
      krypt_lista.remove(0);

      if(found){
        utdata_lista.add(position);
        continue;}

      else{
        continue;}
  }

// ute ur while loop
// kolla om listan är tom eller inte
// om lista tom hittades ingen plats för klartext.

if(utdata_lista.isEmpty()){
  //System.out.println("ingen plats hittades");
  System.out.println("-1");
}
else{
  //System.out.println("följande platser hittades");
  for(int i:utdata_lista){
    System.out.print(i +" ");
  }
}



















  }
}
