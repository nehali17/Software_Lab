import java.util.*;

public class OptimizedCode {
    public static void findDuplicates(List<Integer> list) {
        Set<Integer> seen = new HashSet<>();
        Set<Integer> duplicates = new LinkedHashSet<>();

        for (int value : list) {
            if (!seen.add(value)) {
                duplicates.add(value);
            }
        }

        System.out.println("Duplicate elements are:");
        for (int value : duplicates) {
            System.out.println(value);
        }
    }

    public static void main(String[] args) {
        List<Integer> list = Arrays.asList(1, 2, 3, 4, 2, 5, 6, 3, 7, 1);
        findDuplicates(list);
    }
}

// //Windsurf Optimized Code
// import java.util.*;

// public class CodeOptimization {

//     // Original: O(n^2) time, O(1) extra space
//     public static List<Integer> findDuplicatesBruteForce(List<Integer> list) {
//         List<Integer> duplicates = new ArrayList<>();
//         for (int i = 0; i < list.size(); i++) {
//             boolean seenBefore = false;
//             for (int j = 0; j < i; j++) {
//                 if (list.get(i).equals(list.get(j))) {
//                     seenBefore = true;
//                     break;
//                 }
//             }
//             if (seenBefore) {
//                 continue;
//             }
//             int count = 0;
//             for (int j = 0; j < list.size(); j++) {
//                 if (list.get(i).equals(list.get(j))) {
//                     count++;
//                 }
//             }
//             if (count > 1) {
//                 duplicates.add(list.get(i));
//             }
//         }
//         return duplicates;
//     }

//     // Optimized: O(n) average time, O(n) extra space, preserves first-duplicate order
//     public static List<Integer> findDuplicates(List<Integer> list) {
//         Set<Integer> seen = new HashSet<>();
//         Set<Integer> duplicates = new LinkedHashSet<>();
//         for (Integer value : list) {
//             if (!seen.add(value)) {
//                 duplicates.add(value);
//             }
//         }
//         return new ArrayList<>(duplicates);
//     }

//     // Variant when you also need occurrence counts: O(n) time, O(n) space
//     public static Map<Integer, Integer> duplicateCounts(List<Integer> list) {
//         Map<Integer, Integer> counts = new LinkedHashMap<>();
//         for (Integer value : list) {
//             counts.merge(value, 1, Integer::sum);
//         }
//         counts.values().removeIf(c -> c < 2);
//         return counts;
//     }

//     public static void main(String[] args) {
//         List<Integer> list = Arrays.asList(1, 2, 3, 4, 2, 5, 6, 3, 7, 1);
//         System.out.println("Brute force: " + findDuplicatesBruteForce(list));
//         System.out.println("Optimized:   " + findDuplicates(list));
//         System.out.println("With counts: " + duplicateCounts(list));

//         // sanity checks
//         System.out.println("Empty:       " + findDuplicates(new ArrayList<Integer>()));
//         System.out.println("All same:    " + findDuplicates(Arrays.asList(9, 9, 9)));
//         System.out.println("No dups:     " + findDuplicates(Arrays.asList(1, 2, 3)));
//         System.out.println("With nulls:  " + findDuplicates(Arrays.asList(1, null, 2, null)));
//     }
// }


