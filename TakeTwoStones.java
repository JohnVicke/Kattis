
public class TakeTwoStones {
    public static void main(String[] args) {
        Kattio io = new Kattio(System.in, System.out);
        int n = io.getInt();

        if(n % 2 == 0){
            System.out.println("Bob");
        } else{
            System.out.println("Alice");
        }
    }
}
