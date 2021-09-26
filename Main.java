package com.company;
import java.util.Scanner;
public class Main {
   static Scanner sc = new Scanner(System.in);
   public static void main(String args[])
   {  double a = sc.nextDouble();
      double b = sc.nextDouble();
      double c= a +b;
      double d = a - b;
      double e = a*b;
      double f = a/b;
      double g = Math.pow(a,b);
      System.out.printf("%.3f\n",c);
      System.out.printf("%.3f\n",d);
      System.out.printf("%.3f\n",e);
      System.out.printf("%.3f\n",f);
      System.out.printf("%.3f\n",g);
   }
}