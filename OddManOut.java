import java.util.HashSet;
import java.util.Set;

public class OddManOut {
    public static void main(String[] args) {

        Kattio io = new Kattio(System.in, System.out);
        int n = io.getInt();

        for (int i = 0; i < n; i++) {
            Set<Integer> nrs = new HashSet<>();
            int guests = io.getInt();

            for (int j = 0; j < guests; j++)
                update(nrs, io.getInt());

            io.printf("Case #%d: %d\n", i + 1, nrs.iterator().next());
        }
        io.close();
    }

    public static void update(Set<Integer> set, int nr) {
        if (set.contains(nr)) set.remove(nr);
        else set.add(nr);
    }


}
