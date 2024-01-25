import java.util.*;

public class Baekjoon_4949 {
    public static String inputDataCheck(){
        Scanner inner = new Scanner(System.in);
        String data = inner.nextLine();
        if(data.endsWith(".")){
            return data;
        }
        return null;
    }
    public static void main(String[] args) {
        Map<String, String> dic = new HashMap<>();
        dic.put(")", "(");
        dic.put("]", "[");

        while(true){
            String sentence = inputDataCheck();
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
