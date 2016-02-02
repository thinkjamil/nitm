import java.net.*;
import java.io.*;

public class Server1{
   
	public static void main(String [] args){
		int port = 4421;  
		ServerSocket serverSocket;		
		while(true){
			try{
				serverSocket = new ServerSocket(port);
				serverSocket.setSoTimeout(10000);
				System.out.println("Sever started and waiting");
				Socket server = serverSocket.accept();
				System.out.println("connected to "+ server.getRemoteSocketAddress());
				DataInputStream in = new DataInputStream(server.getInputStream());
				System.out.println(in.readUTF());
				DataOutputStream out = new DataOutputStream(server.getOutputStream());
				out.writeUTF("Access Denied. Goodbye ");
				server.close();
			}
			 catch(IOException e){
				e.printStackTrace();
				break;
			}
		}
	}
}