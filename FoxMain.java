import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class FoxMain {

    static Scanner sc = new Scanner(System.in);
    static List<String> sentence = new ArrayList<>();

    static List<String> getData() {

        List<String> words = new ArrayList<>();
        boolean running = true;

        sentence.add(sc.nextLine());

        while (running) {

            String s = sc.nextLine();
            String[] split = s.split(" ");

            if (!s.equals("what does the fox say?")) words.add(split[split.length - 1]);
            else running = false;

        }

        return words;
    }

    static void whatDoesTheFoxSay(List<String> words, int n) {
        List<String> split = Arrays.asList(sentence.get(n).split(" "));
        String s_ = sentence.get(n);

        for (String s : words) {
            if(split.contains(s)) s_ = s_.replaceAll("\\b" + s + "\\b", "");
        }

        System.out.println(s_.replaceAll("\\s+", " "));

    }

    public static void main(String[] args) {

        int n = sc.nextInt();
        sc.nextLine();
        for (int i = 0; i < n; i++) whatDoesTheFoxSay(getData(), i);
    }
}
