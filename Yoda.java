import java.util.ArrayList;
import java.util.List;

public class Yoda {
    static Kattio io = new Kattio(System.in);
    private String a, b;

    public static void main(String[] args) {
        String in1 = io.getWord();
        String in2 = io.getWord();
        Yoda yoda = new Yoda();
        yoda.addZeros(in1, in2);
        yoda.comparasion();

    }

    void addZeros(String a, String b) {

        if (a.length() > b.length()) b = "0" + b;
        else if (b.length() > a.length()) a = "0" + a;

        else {
            this.a = a;
            this.b = b;
            return;
        }
        addZeros(a, b);
    }

    void comparasion() {

        List<String> aList = new ArrayList<>();
        List<String> bList = new ArrayList<>();

        for (int i = 0; i < a.length(); i++) {
            int a_ = Integer.parseInt(String.valueOf(a.charAt(i)));
            int b_ = Integer.parseInt(String.valueOf(b.charAt(i)));

            if (a_ > b_) {
                aList.add(Integer.toString(a_));
            } else if (a_ < b_) {
                bList.add(Integer.toString(b_));
            } else {
                bList.add(Integer.toString(b_));
                aList.add(Integer.toString(a_));
            }

        }

        if (aList.isEmpty()) System.out.print("YODA");
        else if(!checkIfOnlyZeros(aList)) for (String i : aList) System.out.print(i);
        else System.out.print("0");

        System.out.println();
        if (bList.isEmpty()) System.out.print("YODA");
        else if(!checkIfOnlyZeros(bList)) for (String j : bList) System.out.print(j);
        else System.out.print("0");


    }

    boolean checkIfOnlyZeros(List<String> a) {

        for (String s : a) {
            if (!s.equals("0")) {
                return false;
            }
        }
        return true;
    }
}
