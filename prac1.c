#include <stdio.h>
#include<ctype.h>
#include<string.h>

int main()
{
    char str [100];
    scanf("%s",str);
    int length=strlen(str);
    int i=0;
    if (length==0)
    {
        printf("Invalid string");
    }
    while (i<length && str[i]=='a')
    {
        i++;
    }
    if (i<length && str[i]=='b' && i<length+1 && str[i+1]=='b'&& i+2==length )
    {
        printf("Valid string ");
    } 
    else {
        printf("Invalid string");
    }
    return 0;
}