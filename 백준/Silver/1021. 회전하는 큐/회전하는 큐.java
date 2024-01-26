import java.util.LinkedList;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        LinkedList<Integer> dq = new LinkedList<>();

        int n = in.nextInt();
        int m = in.nextInt();
        int[] idxs = new int[m];
        int cnt = 0;
        
        for (int i = 0; i < m; i++) {
            idxs[i] = in.nextInt();
        }

        for (int i = 1; i < n+1; i++) {
            dq.add(i);
        }
        for(int idx : idxs){
            while(true){
                if(idx==dq.getFirst()){
                    dq.removeFirst();
                    break;
                }

                else if(dq.indexOf(idx) > dq.size()/2){
                    while(dq.getFirst() != idx){
                        dq.addFirst(dq.removeLast());
                        cnt++;
                    }
                }else{
                    while(dq.getFirst() != idx){
                        dq.addLast(dq.removeFirst());
                        cnt++;
                    }
                }
            }
        }

        System.out.println(cnt);
    }
}