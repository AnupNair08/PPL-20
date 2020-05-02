#include<stdio.h>
#include<pthread.h>
#include<unistd.h>

pthread_t second;
pthread_t minutes;
pthread_t hours;

pthread_mutex_t lock1;
pthread_mutex_t lock2;

void *cal_time(void *vargp){
    int i = 0;
    int m = 0;
    int h = 0;
    while(1){
        pthread_mutex_lock(&lock1);
        printf("%d : %d : %d\n",h,m,i);
        sleep(1);
        i++;
        if(i == 60) {
            i = 0;
            m += 1;
            if(m == 60){
                m = 0;
                h += 1;
            }    
        }
        pthread_mutex_unlock(&lock1);
    }
    return NULL;
}


int main(){
    if(pthread_mutex_init(&lock1,NULL) != 0 && pthread_mutex_init(&lock2,NULL) != 0){
        printf("Mutex initialization failed.\n");
        return 0;
    }
    int s = 0;
    int m = 0;
    int h = 0;
    
    int err = pthread_create(&second,NULL,&cal_time,&s);
    if(err != 0){
        printf("Thread initialization failed.\n");
        return 0;
    }

    // err = pthread_create(&minutes,NULL,&cal_time,&s);
    // if(err != 0){
    //     printf("Thread initialization failed.\n");
    //     return 0;
    // }

    // err = pthread_create(&hours,NULL,&cal_time,&s);
    // if(err != 0){
    //     printf("Thread initialization failed.\n");
    //     return 0;
    // }

    pthread_join(second,NULL);
    pthread_mutex_destroy(&lock1);
    pthread_mutex_destroy(&lock2);

    return 0;
}