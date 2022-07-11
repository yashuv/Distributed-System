import java.rmi.Remote;
import java.rmi.RemoteException;

public interface FactorialInterface extends Remote {
    int factorial(int n) throws RemoteException;
}
