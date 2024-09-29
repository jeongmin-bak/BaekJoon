import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String[][] tempArr = new String[5][15];
        for(int i = 0; i < 5; i++){
            String[] arr = sc.next().split("");
            for(int j = 0; j < arr.length; j++) tempArr[i][j] = arr[j];
        }

        for (int i = 0; i < 15; i++) {
            for(int j = 0 ; j < 5 ; j++){
                if (tempArr[j][i] != null){
                    System.out.print(tempArr[j][i]);
                }
            }
        }
    }
}