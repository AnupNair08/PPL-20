// Program that displays hello after every second
#include<stdio.h>
#include<pthread.h>
#include<unistd.h>

pthread_t new;

// Using a func which displays the content every 1 second
void *func(void *vargp){
    int d = *(int *)vargp;
    while(1){
        sleep(1);
        printf("Hello after %d seconds\n",d);
        d++;
    }
    return NULL;
}
int main(){
    int i = 1;
    int err = pthread_create(&new,NULL,func,&i);
    err = pthread_join(new,NULL);
    pthread_exit(NULL);
    return 0;
}