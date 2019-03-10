import java.util.Scanner;

public class Aaah {

    public static int calculateNrOfAs(String string){
        char[] str = string.toCharArray();
        int i = 0;
        for(char c : str){
            if(c == 'a')
                i++;
        }
        return i;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String jonAah = sc.next();
        String docAah = sc.next();

        if ((calculateNrOfAs(jonAah) >= calculateNrOfAs(docAah))){
            System.out.println("go");
        } else{
            System.out.println("no");
        }
    }
}
