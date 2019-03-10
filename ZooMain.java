import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

public class ZooMain {

    static Scanner io = new Scanner(System.in);
    static List<String> outlist = new ArrayList<>();
    static HashMap<String, Integer> nrOufEachAnimal = new HashMap<>();


    static void addExistingAnimal( String animal, List<String> nrAnimalsOut){
        nrOufEachAnimal.replace(animal, nrOufEachAnimal.get(animal), nrOufEachAnimal.get(animal) + 1);
    }

    static void calculateAnimals(List<String> input, int nr){

        List<String> animalsOut = new ArrayList<>();
        outlist.add("List " + nr + ":");
        int i = 1;

        for(String s: input){
            String animal = s.substring(s.lastIndexOf(" ") + 1).toLowerCase();

            if(!animalsOut.contains(animal)){
                nrOufEachAnimal.put(animal, 1);
                animalsOut.add(animal);
            }
            else addExistingAnimal(animal, animalsOut);
        }

        for(String s: animalsOut){
            outlist.add(s + " | " + nrOufEachAnimal.get(s));
        }

    }

    public static void main(String[] args) {
        int n;
        int nr = 1;

        do{
            List<String> animals = new ArrayList<>();

            n = io.nextInt();
            if(n == 0) return;
            io.nextLine();

            for(int i = 0; i < n; i++){
                animals.add(io.nextLine());
            }
            calculateAnimals(animals, nr);
            java.util.Collections.sort(outlist);

            for(String s: outlist) {
                System.out.println(s);
            }

            outlist = new ArrayList<>();

            nr++;

        } while(true);
    }
}
