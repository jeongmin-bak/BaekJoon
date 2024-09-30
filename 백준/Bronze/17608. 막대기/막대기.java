import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        Stack<Integer> sticks = new Stack<>();
        for(int i = 0; i < N; i++){
            int num = sc.nextInt();
            sticks.add(num);
        }
        int maxStick = sticks.pop();
        int cnt = 1;
        while(!sticks.isEmpty()){
            if(sticks.peek() > maxStick){
                maxStick = sticks.pop();
                cnt++;
            }else{
                sticks.pop();
            }
        }
        System.out.println(cnt);
    }
}