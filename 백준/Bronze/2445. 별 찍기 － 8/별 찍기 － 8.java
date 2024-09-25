import java.sql.Array;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int cnt = sc.nextInt();
        List<String> starList = new ArrayList<>();

        for(int i = 1; i <= cnt; i++){
            String star = "*".repeat(i) + " ".repeat(2 * (cnt-i)) + "*".repeat(i);
            System.out.println(star);
            starList.add(star);
        }
        Collections.reverse(starList);

        for(int i = 1; i < starList.size(); i++){
            System.out.println(starList.get(i));
        }
        
    }
}