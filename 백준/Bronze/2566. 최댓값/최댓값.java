import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int maxNum = -1;
        int maxCol = 0;
        int maxRow = 0;

        for(int i = 0; i < 9; i++){
            for(int j = 0; j < 9; j++){
                int num = sc.nextInt();
                if(num > maxNum){
                    maxNum = num;
                    maxCol = i;
                    maxRow = j;
                }
            }
        }

        System.out.println(maxNum);
        System.out.println((maxCol+1)+ " " + (maxRow+1));
    }
}