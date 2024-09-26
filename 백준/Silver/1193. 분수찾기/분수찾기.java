import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int input = sc.nextInt();

        int k = 0;
        int i = 1;
        int sum = 0;

        if(input == 1){
            System.out.println(input+"/"+input);
            return;
        }
        while(true){
            if(sum <= input){
                if((sum + i) >= input){
                    k = i;
                    break;
                }else{
                    sum += i;
                    i++;
                }
            }
        }
        String result = "";
        for(int j = 1; j <= (input - sum); j++){
            if(k%2 != 0){
                result = (k-(j-1)) + "/" + j;
            }else{
                result = j + "/" + (k-(j-1));
            }
        }
        System.out.println(result);
    }
}