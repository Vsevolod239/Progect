import java.util.Scanner;
public class Main {
    static Scanner sc = new Scanner(System.in);
    public static void main(String[] args) {
        int s=0;
        int a;
        do{
            a= sc.nextInt();
            if(a>9&a<100){
                s+=a/10+a%10;
            }
        }while (a/10>=1&a/10<10);
        System.out.println(s);
    }
}
