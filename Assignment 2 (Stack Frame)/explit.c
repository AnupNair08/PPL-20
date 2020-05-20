#include<stdio.h>
#include<unistd.h>

void virus(){
    char *args[2];
    args[0] = "/bin/sh";
    args[1] = NULL;
    execve(args[0],args,NULL);
}
int exploit(){
    int a[1] = {5};
    a[1] = 10;
    a[2] = 0x00000000;
    a[3] = 0x0800064a;
    return a[0];
}

int main(){
    exploit();
    return 0;
}