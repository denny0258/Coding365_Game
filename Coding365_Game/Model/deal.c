#include<stdio.h>
#include<string.h>
int main(){
   char str[10] ={0};
   scanf("%s",str);

   if(strcmp(str,"Hello") ==0 )
      printf("World");
   else
      printf("ERROR");

   return 0;
}
