import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int cnt;
    static int m,n,k;
    static int[][] graph;
    public static void dfs(int x, int y){
        int[] dx = {0, 0, -1, 1};
        int[] dy = {1, -1, 0, 0};

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if((0 <= nx && nx < m) && (0 <= ny && ny < n)){
                if(graph[ny][nx] == 1){
                    graph[ny][nx] = 0;
                    dfs(nx, ny);
                }
            }
        }

    }
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(bf.readLine());
        for (int i = 0; i < t; i++) {
            StringTokenizer st = new StringTokenizer(bf.readLine(), " ");
            m = Integer.parseInt(st.nextToken());
            n = Integer.parseInt(st.nextToken());
            k = Integer.parseInt(st.nextToken());

            graph = new int[n][m];
            cnt = 0;

            for (int j = 0; j < k; j++) {
                st = new StringTokenizer(bf.readLine(), " ");
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                graph[y][x] = 1;
            }

            for (int x = 0; x < m; x++) {
                for (int y = 0; y < n; y++) {
                    if(graph[y][x] == 1){
                        dfs(x, y);
                        cnt++;
                    }
                }
            }
            System.out.println(cnt);
        }
        
    }
}