#include<stdio.h>
#include<pthread.h>
#include<unistd.h>

pthread_t new;
pthread_mutex_t lock;

void *func(void *vargp){
    pthread_mutex_lock(&lock);
    sleep(1);
    printf("Hello after %d seconds\n",*(int *)vargp);
    pthread_mutex_unlock(&lock);
    return NULL;
}
int main(){
    if(pthread_mutex_init(&lock,NULL) != 0){
        printf("Mutex initialization failed.\n");
        return 0;
    }
    int i = 0;
    while(1){
        int err = pthread_create(&new,NULL,func,&i);
        err = pthread_join(new,NULL);
        i++;
    }
    pthread_mutex_destroy(&lock);
    pthread_exit(NULL);
    return 0;
}