public class FixBugs {
    public static void main(String[] args) {

        int[] numbers = {1, 2, 3, 4, 5};
        int sum = 0;

        // Bug: the loop used <=, which tried to access one element past the array end.
        for (int i = 0; i < numbers.length; i++) {
            sum += numbers[i];
        }
        System.out.println("Sum = " + sum);

        String name = "John";
        if ("John".equals(name)) {
            System.out.println("Hello, John!");
        } else {
        }

        // Bug: integer division truncated the result before assigning it to a double.
        double average = sum / (double) numbers.length;
        System.out.println("Average = " + average);
    }
}
