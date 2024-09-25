import java.time.DayOfWeek;
import java.time.LocalDate;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int month = sc.nextInt();
        int day = sc.nextInt();

        String[] days = {"MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"};

        LocalDate date = LocalDate.of(2007, month, day);
        DayOfWeek dayOfWeek = date.getDayOfWeek();
        int dayOfWeekNumber = dayOfWeek.getValue();
        System.out.println(days[dayOfWeekNumber-1]);

    }
}