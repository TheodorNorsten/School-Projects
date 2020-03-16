import java.util.Scanner;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class learn{
  public static void main(String [] args)throws IOException{

    int rad=0;
    int kolumn =0;
    System.out.println("Skriv ett nummer mellan 2 och 10000");

    // läser in data med BufferedReader
    BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
    String[] in= br.readLine().trim().split("\\s+");
    rad = Integer.parseInt(in[0]);
    kolumn =Integer.parseInt(in[1]);


    String[] input_vektor= new String[rad];
    for(int i=0; i<rad; i++){
      System.out.println("rad"+ (i+1));
      input_vektor[i]=br.readLine();
    }



// jämt antal kolumner
if ( kolumn % 2 == 0 ) {
  int helften= kolumn / 2;
  for ( int i = 0; i < rad; i++ ){
      String delsträng_1=input_vektor[i].substring(0,helften);
      String delsträng_2= input_vektor[i].substring(helften,kolumn);
      String reverse="";
      StringBuilder sb= new StringBuilder(delsträng_2);
      reverse= sb.reverse().toString();

      if(delsträng_1.equals(reverse)){
        continue;}
      else{
        System.out.println("Nej");
        return;}
      }
    System.out.println("Ja");

}

// om ojämt antal
else{

  int halva= ((kolumn-1)/2)+1;
  int halva_omv= halva-1;
  for(int i=0;i<rad;i++){

    String delsträng_1=input_vektor[i].substring(0,halva_omv);
    String delsträng_2= input_vektor[i].substring(halva_omv+1,kolumn);
    String reverse="";
    StringBuilder sb= new StringBuilder(delsträng_2);
    reverse= sb.reverse().toString();

    if(delsträng_1.equals(reverse)){
      continue;}
    else{
      System.out.println("Nej");
      return;}
    }
  System.out.println("Ja");
}



  }

}
