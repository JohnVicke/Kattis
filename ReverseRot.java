import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class ReverseRot {

    public static List<Character> alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
            .chars().mapToObj(e -> (char)e).collect(Collectors.toList());

    public static int getIndexInAlpabet(int rotAndIndex){
        while(rotAndIndex >= alphabet.size() ){
            rotAndIndex = rotAndIndex - alphabet.size();
        }
        return rotAndIndex;
    }

    public static String convertion(int rot, String in) {
        char[] normal = in.toCharArray();
        List<Character> converted = new ArrayList<>();
        for(char c: normal){
            int i = 0;
            int pos = 0;
            i = alphabet.indexOf(c);

            if(rot + i >= alphabet.size()){
                pos = getIndexInAlpabet(rot + i);
            } else{
                pos = i + rot;
            }
            converted.add(alphabet.get(pos));
        }


        return converted.stream().map(String::valueOf).collect(Collectors.joining());
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> rotations = new ArrayList<>();
        List<String> input = new ArrayList<>();
        List<String> convertedStrings = new ArrayList<>();

        while (true) {


            int rotation = sc.nextInt();

            if (rotation == 0) {
                break;
            }

            String mess = sc.nextLine().replaceAll(" ", "");

            input.add(new StringBuilder(mess).reverse().toString());
            rotations.add(rotation);


        }

        for (int i = 0; i < input.size(); i++) {
            convertedStrings.add(convertion(rotations.get(i), input.get(i)));
        }

        for(String s: convertedStrings){
            System.out.println(s);
        }
    }
}
