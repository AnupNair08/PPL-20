#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<pthread.h>

int sec = 0;
int hour = 0;
int min = 0;

//Three concurrent threads for keeping track of sec and min
//Sec is shared with minutes and min with hour
pthread_t t1,t2,t3;
pthread_mutex_t lock;	



void *cal_sec() {
	while(1) {
		sleep(1);
		printf("\r%02d:%02d:%02d", hour, min, sec);
		fflush(stdout);
		sec++;
	}
}


void *cal_min() {	
	pthread_mutex_lock(&lock);
	while(1) {
		if(sec == 60){
			sec = 0;
			min++;	
		}
	}
	pthread_mutex_unlock(&lock);
}

void *cal_hour() {
	pthread_mutex_lock(&lock);
	while(1) {
		if(min == 600){
			min = 0;			
			hour++;
		}
	}
    pthread_mutex_unlock(&lock);
}




int main() {
    if(pthread_mutex_init(&lock,NULL) != 0){
        printf("Mutex initialization failed.\n");
        return 0;
    }

	int err  = pthread_create(&t1, NULL, cal_sec, NULL);
    if(err != 0) {
        printf("Thread 1 initialization failed\n");
        return 0;
    }
	err = pthread_create(&t2, NULL, cal_min, NULL);
    if(err != 0) {
        printf("Thread 1 initialization failed\n");
        return 0;
    }
	err = pthread_create(&t3, NULL, cal_hour, NULL);
    if(err != 0) {
        printf("Thread 1 initialization failed\n");
        return 0;
    }
	
	
    printf("Starting Timer..\n");
    printf("HH:MM:SS\n");

	pthread_join(t1, NULL);	
	pthread_join(t2, NULL);
	pthread_join(t3, NULL);
	pthread_mutex_destroy(&lock);
		
	return 0;
}