import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class NewAlphabet {

    public String input = null;
    public Scanner s = new Scanner(System.in);
    public Map<String, String> translationTable = new HashMap<String, String>(){{
        put("a", "@");
        put("b", "8");
        put("c", "(");
        put("d", "|)");
        put("e", "3");
        put("f", "#");
        put("g", "6");
        put("h", "[-]");
        put("i", "|");
        put("j", "_|");
        put("k", "|<");
        put("l", "1");
        put("m", "[]\\/[]");
        put("n", "[]\\[]");
        put("o", "0");
        put("p", "|D");
        put("q", "(,)");
        put("r", "|Z");
        put("s", "$");
        put("t", "']['");
        put("u", "|_|");
        put("v", "\\/");
        put("w", "\\/\\/");
        put("x", "}{");
        put("y", "`/");
        put("z", "2");
    }};

    public static void main(String[] args) {
        NewAlphabet na = new NewAlphabet();
        na.input = na.s.nextLine().toLowerCase();
        char[] charArray = na.input.toCharArray();
        String outputString = "";
        for (char c : charArray){
            String test = na.translationTable.get(Character.toString(c));
            if(!(test == null)){
                outputString += test;
            }
            else {
                outputString += c;
            }
        }
        System.out.println(outputString);
    }
}
