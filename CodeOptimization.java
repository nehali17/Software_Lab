import java.util.*;
public class CodeOptimization {
    public static void findDuplicates(List<Integer> list) {
        for (int i = 0; i < list.size(); i++) {
            boolean isDuplicate = false;
            for (int j = 0; j < i; j++) {
                if (list.get(i).equals(list.get(j))) {
                    isDuplicate = true;
                    break;
                }
            }
            if (isDuplicate) {
                continue;
            }
            int count = 0;
            for (int j = 0; j < list.size(); j++) {
                if (list.get(i).equals(list.get(j))) {
                    count++;
                }
            }

            if (count > 1) {
                System.out.println(list.get(i));
            }
        }
    }
    public static void main(String[] args) {
        List<Integer> list = Arrays.asList(1, 2, 3, 4, 2, 5, 6, 3, 7, 1);
        System.out.println("Duplicate elements are:");
        findDuplicates(list);
    }
}