import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;

import static java.lang.Math.abs;
import static java.lang.Math.pow;

public class Boj3425 {
    static LinkedList<Long> stack;
    static int stackSize;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<String> cmdList = new ArrayList<>();
        String[] input = br.readLine().split(" ");

        stack = new LinkedList<>();

        while(!input[0].equals("QUIT")) {
            if(input[0].equals("")) {
                cmdList.clear();
                System.out.println();
            }
            else if(input[0].equals("END")) {
                int N = Integer.parseInt(br.readLine().split(" ")[0]);

                for(int n=0; n < N; n++) {
                    stack.clear();
                    long initNum = Long.parseLong(br.readLine().split(" ")[0]);
                    stack.add(initNum);
                    System.out.println(runCommand(cmdList));
                }

            }
            else {
                cmdList.add(input[0]);
                if(input[0].equals("NUM")) {
                    cmdList.add(input[1]);
                }
            }
            input = br.readLine().split(" ");

        }

    }

    private static String runCommand(ArrayList<String> cmd) {
        int idx = 0;
        while (idx < cmd.size()) {
            try {
                switch (cmd.get(idx)) {
                    case "NUM": {
                        long x = Long.parseLong(cmd.get(++idx));
                        stack.add(x);
                        break;
                    }
                    case "POP": {
                        stack.removeLast();
                        break;
                    }
                    case "INV": {
                        long tmp = stack.removeLast();;
                        stack.add(tmp*-1);
                        break;
                    }
                    case "DUP": {
                        stack.add(stack.getLast());
                        break;
                    }
                    case "SWP": {
                        long num1 = stack.removeLast();
                        long num2 = stack.removeLast();

                        stack.add(num1);
                        stack.add(num2);
                        break;
                    }
                    case "ADD": {
                        long num1 = stack.removeLast();
                        long num2 = stack.removeLast();

                        stack.add(num1+num2);
                        stackSize--;
                        break;
                    }
                    case "SUB": {
                        long num1 = stack.removeLast();
                        long num2 = stack.removeLast();

                        stack.add(num2-num1);
                        stackSize--;
                        break;
                    }
                    case "MUL": {
                        long num1 = stack.removeLast();
                        long num2 = stack.removeLast();

                        stack.add(num2*num1);
                        stackSize--;
                        break;
                    }
                    case "DIV": {
                        long num1 = stack.removeLast();
                        long num2 = stack.removeLast();


                        long tmp = abs(num2)/abs(num1);
                        if(num1*num2 < 0) {
                            tmp *= -1;
                        }
                        stack.add(tmp);
                        break;

                    }
                    case "MOD": {
                        long num1 = stack.removeLast();
                        long num2 = stack.removeLast();


                        long tmp = abs(num2)%abs(num1);
                        if(num2<0) {
                            tmp *= -1;
                        }

                        stack.add(tmp);
                        stackSize--;
                        break;
                    }
                }
            } catch (Exception e) {
                return "ERROR";
            }
            idx++;
        }

        if(stack.size() == 1) {
            if(abs(stack.getLast()) > pow(10, 9)) {
                return "ERROR";
            }
            return stack.getLast().toString();

        }
        return "ERROR";


    }
}
