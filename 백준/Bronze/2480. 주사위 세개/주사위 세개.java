import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num1 = sc.nextInt();
        int num2 = sc.nextInt();
        int num3 = sc.nextInt();

        Set<Integer> nums = new HashSet<Integer>();
        nums.add(num1);
        nums.add(num2);
        nums.add(num3);

        if(nums.size() == 3){
            Integer maxNum = nums
                    .stream()
                    .mapToInt(x -> x)
                    .max()
                    .orElseThrow(NoSuchFieldError::new);
            System.out.println(maxNum * 100);
        }else if(nums.size() == 2){
            if((num1 == num3) || (num1 == num2)){
                System.out.println(1000 + num1 * 100);
            }else if(num2 == num3){
                System.out.println(1000 + num2 * 100);
            }else{
                System.out.println(1000 + num3 * 100);
            }
        }else{
            System.out.println(10000 + num1 * 1000);
        }
    }
}