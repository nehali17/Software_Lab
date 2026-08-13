public class messy {
    public static void main(String[] args) {
        int[] arr = {12, 5, 8, 3, 10, 7};

        int first = Integer.MAX_VALUE;
        int second = Integer.MAX_VALUE;

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] < first) {
                second = first;
                first = arr[i];
            } else if (arr[i] < second && arr[i] != first) {
                second = arr[i];
            }
        }

        System.out.println("Second Smallest = " + second);
    }
}