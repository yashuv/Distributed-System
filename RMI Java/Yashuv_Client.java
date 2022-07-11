import java.util.*;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Yashuv_Client {
    private Yashuv_Client() {
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        try {
            Registry registry = LocateRegistry.getRegistry(null);
            FactorialInterface stub = (FactorialInterface) registry.lookup("FactorialInterface");

            while (true) {
                System.out.print("Enter nummber for factorial: ");
                int n = in.nextInt();
                System.out.println(stub.factorial(n));
            }
        } catch (Exception e) {
            System.err.println("Client exception: " + e.toString());
            e.printStackTrace();
        } finally {
            in.close();
        }
    }
}
