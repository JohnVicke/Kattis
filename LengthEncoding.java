import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class LengthEncoding {
    static String state;
    static Scanner sc = new Scanner(System.in);

    static void decode(String s){
        List<Character> decoded = new ArrayList<>();

        for(int i = 0; i < s.length(); i = i + 2){

            if(i + 1  >= s.length()){
                break;
            }

            for(int j = 0; j < Character.getNumericValue(s.charAt(i+1)); j++){
                decoded.add(s.charAt(i));
            }
        }
        for (char c: decoded) {
            System.out.print(c);
        }
    }

    static void encode(String s) {

        List<String> occurances = new ArrayList<>();
        int j = 1;

        for (int i = 0; i < s.length(); i++) {

            if (i + 1 >= s.length()){
                occurances.add(s.charAt(i) + Integer.toString(j));
                break;
            }

            if (s.charAt(i) == s.charAt(i + 1)) {
                j++;

            } else {
                occurances.add(s.charAt(i) + Integer.toString(j));
                j = 1;
            }

        }

        for (String f : occurances) {
            System.out.print(f);
        }

    }


    public static void main(String[] args) {
        state = sc.next();
        String input = sc.next();

        switch (state) {
            case "E":
                encode(input);
                break;
            case "D":
                decode(input);
                break;
        }

    }

}
