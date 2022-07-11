import java.rmi.registry.Registry;
import java.rmi.registry.LocateRegistry;
import java.rmi.server.UnicastRemoteObject;

public class Baskota_Server extends Factorial {
    public Baskota_Server() {
    }
    public static void main(String args[]) {
        try {
            Factorial obj = new Factorial();
            FactorialInterface stub = (FactorialInterface) UnicastRemoteObject.exportObject(obj, 0);
            Registry registry = LocateRegistry.getRegistry();
            registry.bind("FactorialInterface", stub);
            System.err.println("Server is ready...");
        } catch (Exception e) {
            System.err.println("Server exception: " + e.toString());
            e.printStackTrace();
        }
    }
}
