import java.util.Scanner;

public class SevenWonders {
    static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        String s = scanner.next();
        String[] split = s.split("");
        int T = 0, C = 0, G = 0;

        for (String card : split) {
            if (card.equals("T"))
                T++;
            else if (card.equals("C"))
                C++;
            else
                G++;
        }

        if (T != 0 && C != 0 && G != 0) {
            int nrSets = Math.min(T, Math.min(C,G));
            System.out.println((T * T) + (C * C) + (G * G) + (nrSets* 7));

        } else{
            System.out.println((T * T) + (C * C) + (G * G));
        }



    }
}
