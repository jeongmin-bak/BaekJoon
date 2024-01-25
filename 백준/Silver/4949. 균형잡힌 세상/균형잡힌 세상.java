import java.util.*;
public class Main {
    public static void main(String[] args) {
        Map<String, String> dic = new HashMap<>();
        dic.put(")", "(");
        dic.put("]", "[");
        
        Scanner inner = new Scanner(System.in);
        while(true){
            String sentence = inner.nextLine();
            if (sentence.equals(".")){
                break;
            }

            Stack stack = new Stack();
            Boolean flag = true;
            for (String alpha: sentence.split("")) {
                if (alpha.equals("(") || alpha.equals("[")){
                    stack.push(alpha);
                } else if (alpha.equals(")") || alpha.equals("]")) {
                    if (stack.isEmpty()){
                        flag = false;
                        break;
                    }
                    if (stack != null && dic.get(alpha).equals(stack.peek())){
                        stack.pop();
                    }else{
                        flag = false;
                        break;
                    }
                }
            }

            if (flag == false || !stack.isEmpty()){
                System.out.println("no");
            }else{
                System.out.println("yes");
            }
        }
    }
}