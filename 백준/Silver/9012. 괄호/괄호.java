import java.util.Arrays;
import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        int cnt = sc.nextInt();

        for (int i = 0; i < cnt; i++) {
            String s = sc.next();
            String[] token = s.split("");
            Stack<String> stack = new Stack<>();

            for(String c : token){
                if(c.equals("(")){
                    stack.push(c);
                }
                if(c.equals(")")){
                    if(stack.isEmpty()){
                        stack.push(c);
                    }
                    if((stack.peek()).equals("(")){
                        stack.pop();
                    }
                }
            }

            if(stack.isEmpty()){
                sb.append("YES").append("\n");
            }else{
                sb.append("NO").append("\n");
            }
        }
        System.out.println(sb);
    }
}
