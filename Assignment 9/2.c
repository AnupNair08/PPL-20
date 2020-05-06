#include<stdio.h>
#include<unistd.h>
#include<pthread.h>


pthread_t hello;
pthread_t goodbye;
pthread_mutex_t lock;

void *printfunc(void *vargp){
    while(1){
    pthread_mutex_lock(&lock);
    printf("---------------------Thread started--------------------\n\n");
    printf("%s\n\n",(char *)vargp);
    printf("---------------------Thread ended-----------------------\n\n");
    pthread_mutex_unlock(&lock);
    sleep(1);
    }
}

int main(){
    char s[20] = "Hello World";
    char g[20] = "Goodbye World";
    if(pthread_mutex_init(&lock,NULL) != 0){
        printf("Mutex initialization failed.\n");
        return 0;
    }

    int err = pthread_create(&hello,NULL,&printfunc,&s);
    if(err != 0) {
        printf("Thread 1 initialization failed\n");
        return 0;
    }

    err = pthread_create(&goodbye,NULL,&printfunc,&g);
    if(err != 0) {
        printf("Thread 2 initialization failed\n");
        return 0;
    }

    pthread_join(hello,NULL);
    pthread_join(goodbye,NULL);
    pthread_mutex_destroy(&lock);
}