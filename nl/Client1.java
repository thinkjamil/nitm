import java.net.*;
import java.io.*;

public class Client1{
   public static void main(String [] args){
      int port = 4421;
	  String serverName = "localhost";
      try{
         Socket client = new Socket(serverName, port);
         System.out.println("Connected to Server");
         OutputStream outToServer = client.getOutputStream();
         DataOutputStream out = new DataOutputStream(outToServer);
         out.writeUTF("Hello Im a client");
         InputStream inFromServer = client.getInputStream();
         DataInputStream in = new DataInputStream(inFromServer);
         System.out.println("Server : " + in.readUTF());
         client.close();
      }catch(IOException e){
         e.printStackTrace();
      }
   }
}