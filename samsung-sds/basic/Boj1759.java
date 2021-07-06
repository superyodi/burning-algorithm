// 백준 - 암호 만들기

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Boj1759 {
    static int L,C;
    static char[] answers;
    static char[] alphas;



    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        L = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        answers = new char[L];
        alphas = new char[C];

        st = new StringTokenizer(br.readLine());
        for(int i=0; i < C; i++) {
            String str = st.nextToken();
            alphas[i] = str.charAt(0);
        }
        Arrays.sort(alphas);

        recur(0,0);


    }

    public static void recur(int where, int from) {
        if(where == L) {
            if (check()) {
                System.out.println(new String(answers));
            }

            return;
        }
        for(int i = from; i < C; i++) {
            answers[where] = alphas[i];
            recur(where+1, i+1);
        }
    }

    static boolean check() {
        int countMo = 0, countJa = 0;
        boolean[] isMo = new boolean[128];
        isMo['a'] = true;
        isMo['e'] = true;
        isMo['i'] = true;
        isMo['o'] = true;
        isMo['u'] = true;

        for(int i=0; i < L; i++) {
            if(isMo[answers[i]]) countMo++;
            else countJa++;
        }

        return countMo>=1 && countJa >= 2;
    }
}
