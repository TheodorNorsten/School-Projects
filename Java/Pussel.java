import java.util.Scanner;
import java.util.Arrays;
import java.util.ArrayList;


public class Pussel{
  public static void main(String[] args){
    int k=0;
    int n=0;
    double summa_k=0;
    double summa_n =0;
    long [] vektor= new long[5];


    long year;
    long  days;
    long  hours;
    long  min;
    long  sek;
    int sek_year=3600*24*365;
    int sek_day= 3600*24;
    int x=0;
    int y=0;
    Scanner input= new Scanner(System.in);

    while(true){
      //System.out.println("välj 2 tal mellan 1-100");
    try{
      String check_x= input.next();
      String check_y= input.next();
      x= Integer.parseInt(check_x);
      y= Integer.parseInt(check_y);
    }
    catch(Exception e){
      //System.out.println("input måste vara en siffra,försök igen\n ");
      continue;
    }

    if(x<1||x>100){
      //System.out.println("fel inmatning");
      continue;
    }
    else if(y<1||y>100){
      //System.out.println("fel inmatning");
      continue;
    }
    break;
  }
  if(x<3 ||y<3){
    k=x*y;

  }
  else{
     k= 2*(x+y)-4;
     n= (x-2)*(y-2);

}
  //System.out.println("k och n is " + k + "och" + n);
  for(int i=1;i<=k;i++){
    summa_k+=Math.pow(1.001,i);
  }
  //System.out.println("totala tid för kantbitar "+ summa_k);

  for(int i=1;i<=n;i++){
    summa_n+= Math.pow(1.01,i);
}
  //System.out.println("tid för innerbitar"+ summa_n);

  long tot_tid=(long)(summa_k+summa_n);
  //System.out.println(tot_tid);


  year= tot_tid/sek_year;
  long år= (int)year;
  vektor[0]=år;
  tot_tid-=år*sek_year;

  days= tot_tid/sek_day;
  long dag= (int)days;
  vektor[1]=dag;
  tot_tid-=dag*sek_day;

  hours= tot_tid/3600;
  long timme= (int) hours;
  vektor[2]=timme;
  tot_tid-=timme*3600;

  min= tot_tid/60;
  long minut= (int)min;
  vektor[3]=minut;
  tot_tid-=minut*60;

  sek=tot_tid;
  long sekunder= (int) sek;
  vektor[4]=sekunder;
  tot_tid-=sekunder*60;

  for(long i: vektor){
  System.out.print(i+ " ");}


}
}
