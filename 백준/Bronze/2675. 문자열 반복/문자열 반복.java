import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int cnt = sc.nextInt();

        for(var i = 0; i < cnt; i ++){
            int repeatCnt = sc.nextInt();
            String s = sc.next();

            String result = "";
            String[] sList = s.split("");
            for(String c : sList){
                result += c.repeat(repeatCnt);
            }
            System.out.println(result);
        }

    }
}