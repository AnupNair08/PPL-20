#include<stdio.h>

int fact(int a){
    if(a == 1 || a == 0) return 1;
    else return a * fact(a - 1);
}

int main(){
    int n = 5;
    fact(5);
    // printf("%d",fact(5));
    return 0;
}