import java.util.Scanner;

public class TemperatureCalculator {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter temperature in Celsius: ");
        int celsius = sc.nextInt();

        // Bug: the formula used the wrong conversion ratio and integer division, which produced incorrect Fahrenheit values.
        double fahrenheit = celsius * 9.0 / 5 + 32;

        System.out.println("Temperature in Fahrenheit: " + fahrenheit);

        // Bug: the condition was checking the wrong threshold, so temperatures below freezing were not handled correctly.
        if (celsius < 0) {
            System.out.println("Freezing Temperature");
        } else {
            System.out.println("Normal Temperature");
        }

        int x = 10;
        // Bug: dividing by zero caused a runtime error instead of producing a valid result.
        int y = 1;
        System.out.println("Result: " + (x / y));

        sc.close();
    }
}

