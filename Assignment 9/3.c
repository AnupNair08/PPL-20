//Program to display a timer using three concurrent threads
#include<stdio.h>
#include<pthread.h>
#include<unistd.h>


//All 4 threads run concurrently.
pthread_t second;
pthread_t minute;
pthread_t hour;
pthread_t print;
int h = 0;
int m = 0;
int s = -1;
//Seconds and minutes are the shared resources among all the three threads.
//The seconds thread updates it after every second and it is tracked by hours and minutes thread
void *cal_hour(void *vargp){
    while(1){
        if(m == 60){
            h += 1;
            m = 0;
        }
    }
}

void *cal_min(void *vargp){
        while(1){
        if( s == 60){
            m += 1;
            s = 0;
            if(m == 60) m = 0;
        }
        }
}

void *cal_sec(void *vargp){
    while(1){
        s++;
        sleep(1);
    }
}

void *print_time(void *vargp){
    while(1){
        sleep(1);
        printf("%d : %d : %d\n",h,m,s%60);
    }
}

int main(){
    printf("Starting Timer..\n");
    printf("HR: MM: SS..\n");
    sleep(1);

    pthread_create(&second,NULL,&cal_sec,NULL);
    pthread_create(&minute,NULL,&cal_min,NULL);
    pthread_create(&hour,NULL,&cal_hour,NULL);
    pthread_create(&print,NULL,&print_time,NULL);

    pthread_join(second,NULL);
    pthread_join(minute,NULL);
    pthread_join(hour,NULL);
    pthread_join(print,NULL);

    pthread_exit(NULL);
    return 0;
}