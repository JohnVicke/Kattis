import java.util.*;
import java.util.concurrent.LinkedBlockingDeque;
import java.util.concurrent.LinkedBlockingQueue;

public class HappyPrime {

    static Scanner sc = new Scanner(System.in);
    static Stack<Integer> digits = new Stack<>();

    static void addToStack(int sum) {
        digits.removeAllElements();
        while (sum > 0) {
            if (sum != 0) {
                digits.add(sum % 10);
            }
            sum = sum / 10;
        }
    }

    static boolean isHappyHappyPrime(int n) {
        if (n == 2) return false;

        if (n < 7) return false;

        addToStack(n);
        int k = 7;

        while (k > 6) {

            int stackSize = digits.size();
            k = 0;

            for (int i = 0; i < stackSize; i++) {
                int firstnr = digits.pop();
                firstnr = firstnr * firstnr;
                k = k + firstnr;
            }

            if (k == 1) return true;

            addToStack(k);

        }

        return false;
    }

    static boolean isPrime(int n) {
        if (n == 0 || n == 1) return false;

        if (n == 2) return true;

        for (int i = 2; i < n; i++)
            if (n % i == 0) return false;

        return true;
    }

    public static void main(String[] args) {
        int nrOfIterations = sc.nextInt();
        int[] candidates = new int[nrOfIterations];
        for (int i = 0; i < nrOfIterations; i++) {
            sc.nextInt();
            candidates[i] = sc.nextInt();
        }
        int i = 1;
        for (int n : candidates) {

            if (isPrime(n)) {

                if (isHappyHappyPrime(n)) System.out.println(i + " " + n + " YES");


                else System.out.println(i + " " + n + " NO");


            } else System.out.println(i + " " + n + " NO");

            i++;
        }
    }
}
