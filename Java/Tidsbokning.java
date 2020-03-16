import java.util.Scanner;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;
import java.util.Collections;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;


public class Tidsbokning{
  public static void main(String [] args)throws IOException{

    //System.out.println("skriv antalet mötestider och antalet deltagare");
    // Initerar 2 scanner variabler.
    BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
    String[] in= br.readLine().trim().split("\\s+");

    // Initierar variableran antalet mötestider och deltagare
    int motestider=Integer.parseInt(in[0]);
    int deltagare=Integer.parseInt(in[1]);
    int tot_rad= motestider+ deltagare;

    if(motestider<=0 || deltagare<=0){
      //System.out.println("indata får inte vara noll ");
      return;
    }

    // 1.läser in vaje rad till strängen input_vektor.
    //2. lägger till varje element i input_vektor till attributen för objektet motestider.
    //3. Adderar varje obj till listan meetingtime.

    ArrayList<MeetingTime> meetingtime=new ArrayList<MeetingTime>();
    ArrayList<String> pref_lista= new ArrayList<String>();

    //System.out.println("skriv alla mötestider");

    for(int i=0; i<tot_rad; i++){


      if(i<=motestider-1){
      MeetingTime objekt= new MeetingTime();

      String[] input_vektor= br.readLine().trim().split("\\s+");

      objekt.lopnummer=Integer.parseInt(input_vektor[0]); // Integer
      objekt.veckodag=input_vektor[1];
      objekt.datum= Integer.parseInt(input_vektor[2]);//Integer
      objekt.Month= input_vektor[3];
      objekt.tid= input_vektor[4];

      meetingtime.add(objekt);
    }
else{

    String[] temp_vek= br.readLine().trim().split("\\s+");
    for(int j=1; j<temp_vek.length; j++){
      pref_lista.add(temp_vek[j]);
}


}

  }



// konverterar lista med sträng till lista med Integer för alla roster.
// för att kunna använda Collections.frequency.
ArrayList<Integer> rost_lista= new ArrayList<Integer>();
for(String s:pref_lista){
  rost_lista.add(Integer.valueOf(s));
}

// Adderar attributet roster till varje objekt med Collections.
for(int i=0; i<motestider;i++){
  int freq= Collections.frequency(rost_lista,i);
  meetingtime.get(i).roster=freq;
}

// sorterar listan occh skriver ut lista med mötestider.
Collections.sort(meetingtime);
for(MeetingTime i:meetingtime){
  System.out.println(i);
}



}
  }



  // klass MeetingTime.
  // Representerar möjlig tid för mötet.
  class MeetingTime implements Comparable<MeetingTime>{
  // attributen för varje mötestidOjekt.
    int lopnummer;
    String veckodag;
    int datum;
    String Month;
    String tid;
    int roster;

  // Metod
  // sorterar i fallande ordning.
  // Sorterar först efter roster, annars efter lopnummer.
  public int compareTo(MeetingTime other){
    if(this.roster < other.roster){
      return 1;}

    else if(this.roster > other.roster){
      return -1;}

    else{
      if(this.lopnummer < other.lopnummer){
        return -1;}
      else if (this.lopnummer > other.lopnummer) {
        return 1;}
      else{
        return 0;}
  }
    }

    // Metod som skriver ut objekten.
    public String toString(){
     return lopnummer +" "+ veckodag +" "+ datum +" " + Month +" " + tid +  " "+ roster;
    }

      }
