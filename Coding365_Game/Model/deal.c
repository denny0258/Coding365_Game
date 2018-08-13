#include<stdio.h>
#include<string.h>
int main(){
char str[10] ={};
scanf("%s",str);

if(strcmp(str,"Holle") ==0 )
    printf("world");
else
    printf("ERROR");

return 0;
}
