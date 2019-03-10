import java.util.ArrayList;
import java.util.List;

public class NastyHacks {
    private Kattio io;
    private List<int[]> cases = new ArrayList<>();

    private NastyHacks() {
        io = new Kattio(System.in);
        collectData();
    }

    private void collectData() {
        int iterations = io.getInt();
        for (int i = 0; i < iterations; i++) {
            int[] testCase = new int[3];
            testCase[0] = io.getInt();
            testCase[1] = io.getInt();
            testCase[2] = io.getInt();

            cases.add(testCase);
        }
    }

    private void solveProblem() {
        for (int[] i : cases) {
            int no = i[0];
            int yes = i[1];
            int cost = i[2];

            if (no > (yes - cost)) System.out.println("do not advertise");
            else if (no == (yes - cost)) System.out.println("does not matter");
            else System.out.println("advertise");
        }
    }

    public static void main(String[] args) {
        NastyHacks nh = new NastyHacks();
        nh.solveProblem();
    }
}
