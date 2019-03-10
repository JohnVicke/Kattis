import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class HappyHappyPrimePrime {

    private static List<String> primes = new ArrayList<>();
    private static List<Integer> initials = new ArrayList<>();

    public static boolean isHappy(String number) {

        int a, b, c, d, e, f;
        int n = 0;

        while (n < 50) {
            n++;
            switch (number.length()) {
                case 1:
                    //0 - 9
                    if (number.equals("1")) {
                        //System.out.println(n);
                        return true;
                    } else {
                        a = Integer.parseInt(number);
                        b = (a * a);
                        number = Integer.toString(b);
                        continue;
                    }
                case 2:
                    //10 - 99
                    a = Character.getNumericValue(number.charAt(0));
                    b = Character.getNumericValue(number.charAt(1));
                    c = (a * a) + (b * b);
                    number = Integer.toString(c);
                    continue;
                case 3:
                    //100 - 999
                    a = Character.getNumericValue(number.charAt(0));
                    b = Character.getNumericValue(number.charAt(1));
                    c = Character.getNumericValue(number.charAt(2));
                    d = (a * a) + (b * b) + (c * c);
                    number = Integer.toString(d);
                    continue;
                case 4:
                    //1000 - 9999
                    a = Character.getNumericValue(number.charAt(0));
                    b = Character.getNumericValue(number.charAt(1));
                    c = Character.getNumericValue(number.charAt(2));
                    d = Character.getNumericValue(number.charAt(3));
                    e = (a * a) + (b * b) + (c * c) + (d * d);
                    number = Integer.toString(e);
                    continue;
                case 5:
                    //10 000 - 99 999
                    a = Character.getNumericValue(number.charAt(0));
                    b = Character.getNumericValue(number.charAt(1));
                    c = Character.getNumericValue(number.charAt(2));
                    d = Character.getNumericValue(number.charAt(3));
                    e = Character.getNumericValue(number.charAt(4));
                    f = (a * a) + (b * b) + (c * c) + (d * d) + (e * e);
                    number = Integer.toString(f);
                    continue;
            }
        }
        return false;
    }

    public static boolean isPrime(int a) {
        if (a == 2) {
            return true;
        } else if (a % 2 == 0) {
            return false;
        }

        for (int i = 3; i * i <= a; i += 2) {
            if (a % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static void fillArray() {
        int bigInt = 1;
        for(int i = 0; i < 10; i++){
            initials.add(bigInt);
            bigInt = bigInt*10;
        }
    }

    public static void main(String[] args) {

        fillArray();
        Scanner s = new Scanner(System.in);
        int listSize = Integer.parseInt(s.nextLine());

        for (int i = 0; i < listSize; i++) {
            primes.add(s.nextLine());
        }

        for (int i = 0; i < listSize; i++) {
            String[] cutter = primes.get(i).split(" ");
            int nextInt = Integer.parseInt(cutter[1]);
            String nextString = cutter[1];

            if (initials.contains(nextInt) || !isPrime(nextInt)) {
                System.out.println((i + 1) + " " + nextString + " " + "NO");
                continue;
            } else {
                if (isHappy(nextString)) {
                    System.out.println((i + 1) + " " + nextInt + " YES");
                    continue;
                } else {
                    System.out.println((i + 1) + " " + nextInt + " " + "NO");
                    continue;
                }
            }

        }
    }
}
