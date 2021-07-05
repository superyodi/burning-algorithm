
// 백준 - 가르침

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

import static java.lang.Integer.max;

public class Boj062 {
    static int N,K;
    static int maxCount = 0;
    static boolean visited[] = new boolean[26];
    static String[] words;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        words = new String[N];

        if(K < 5) {
            System.out.println(0);
            return;
        }

        if(K == 26) {
            System.out.println(N);
            return;
        }

        for (int i=0; i < N; i++) {
            String str = br.readLine();
            words[i] = str.substring(4, str.length()-4); // "anta", "tica" 제거
        }

        K -= 5;
        visited['a' - 'a'] = true;
        visited['n' - 'a'] = true;
        visited['t' - 'a'] = true;
        visited['i' - 'a'] = true;
        visited['c' - 'a'] = true;

        dfs(0,0);
        System.out.println(maxCount);
    }

    private static void dfs(int head, int count) {
        if(count == K) {
            int nowCount = 0;
            for(int i=0; i < N; i++) {
                boolean isOkay = true;
                for(int j = 0; j < words[i].length(); j++) {
                    int alpha = words[i].charAt(j) - 'a';
                    if (!visited[alpha]) {
                        isOkay = false;
                        break;
                    }
                }
                if(isOkay) nowCount++;
            }
            maxCount = max(maxCount, nowCount);
            return;
        }

        for (int i = head; i < 26; i++) {
            if(!visited[i]) {
                visited[i] = true;
                dfs(i, count+1);
                visited[i] = false;
            }
        }
    }


}
