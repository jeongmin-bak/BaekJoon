import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String input = bf.readLine();
        Stack<Character> stack = new Stack<>();
        int cnt = 0;
        for (int i = 0; i < input.length(); i++) {
            if(input.charAt(i)=='('){
                stack.push(input.charAt(i));
            }else{
                if(input.charAt(i-1) == '('){
                    stack.pop();
                    cnt += stack.size();
                }else{
                    stack.pop();
                    cnt += 1;
                }
            }
        }

        bw.write(cnt + "\n");
        bw.flush();
        bf.close();
        bw.close();

    }
}