#include<stdio.h>
#include<pthread.h>
#include<unistd.h>



pthread_t second;
pthread_t minute;
pthread_t hour;
pthread_mutex_t lock;

int h = -1;
int m = -1;
int s = 0;

void *cal_hour(void *vargp){
        if((s) % 3600 == 0) h+= 1;
}

void *cal_min(void *vargp){
        if((s) % 60 == 0){
            m += 1;
            if(m == 60) m = 0;
        }
}

void *cal_sec(void *vargp){
    s++;
    sleep(1);
    printf("%d : %d : %d\n",h,m,s%60);
}

int main(){
    int k;
    pthread_mutex_init(&lock,NULL);
    while(1){
        pthread_create(&hour,NULL,&cal_hour,NULL);
        pthread_create(&minute,NULL,&cal_min,NULL);
        pthread_create(&second,NULL,&cal_sec,NULL);
        pthread_join(second,NULL);
    }
    // pthread_join(second,NULL);
    // pthread_join(minute,NULL);
    // pthread_join(hour,NULL);
    

    pthread_mutex_destroy(&lock);
    return 0;
}