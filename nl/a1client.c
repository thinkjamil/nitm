#include <stdio.h>
#include <stdlib.h>
#include <netdb.h>
#include <netinet/in.h>
#include <string.h>

int main()
{
   int sockfd, portno, n;
   struct sockaddr_in serv_addr;
   struct hostent *server;
   
   char buffer[1024];
   portno = 12345;
   sockfd = socket(AF_INET, SOCK_STREAM, 0);
   if (sockfd < 0)
   {
      printf("socket error");
      return 1;
   }
   server = gethostbyname("localhost");
   bzero((char *) &serv_addr, sizeof(serv_addr));
   serv_addr.sin_family = AF_INET;
   bcopy((char *)server->h_addr, (char *)&serv_addr.sin_addr.s_addr, server->h_length);
   serv_addr.sin_port = htons(portno);   
   if (connect(sockfd, (struct sockaddr*)&serv_addr, sizeof(serv_addr)) < 0)
   {
      printf("connection error");
      return 1;
   }
   printf("Please enter the message: ");
   bzero(buffer,1024);
   fgets(buffer,1024,stdin);;
   n = write(sockfd, buffer, strlen(buffer));
   bzero(buffer,1024);
   n = read(sockfd, buffer, 1023);	
   printf("Client :%s\n",buffer);
   return 0;
}
