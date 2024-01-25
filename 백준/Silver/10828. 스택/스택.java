import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static int checkEmpty(Stack stack){
        if(stack.isEmpty()){
            return 1;
        }
        else{
            return 0;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int count = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < count; i++){
            String str = br.readLine();
            String[] token = str.split(" ");
            String word = token[0];

            switch (word){
                case "push":
                    stack.push(Integer.parseInt(token[token.length-1]));
                    break;
                case "pop":
                    if(checkEmpty(stack) == 1){
                        sb.append(-1).append("\n");
                    }
                    else{
                        sb.append(stack.pop()).append("\n");
                    }
                    break;
                case "top":
                    if(checkEmpty(stack) == 1){
                        sb.append(-1).append("\n");
                    }
                    else{
                        sb.append(stack.peek()).append("\n");
                    }
                    break;
                case "size":
                    sb.append(stack.size()).append("\n");
                    break;
                case "empty":
                    sb.append(checkEmpty(stack)).append("\n");

            }
        }
        System.out.println(sb);
    }
}