public class clean {
    public static void main(String[] args) {
        int[] arr = {12, 5, 8, 3, 10, 7};

        int smallest = Integer.MAX_VALUE;
        int secondSmallest = Integer.MAX_VALUE;

        for (int value : arr) {
            if (value < smallest) {
                secondSmallest = smallest;
                smallest = value;
            } else if (value < secondSmallest && value != smallest) {
                secondSmallest = value;
            }
        }

        String result = "Second Smallest = " + secondSmallest;
        System.out.println(result);
    }
}