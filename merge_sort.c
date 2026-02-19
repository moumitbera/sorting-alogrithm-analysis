#include <stdio.h>
#include <time.h>
#include <stdlib.h>


typedef struct{
    long comparisons;
    long writes;
} Metrics;

void generate_random(int arr[], int n){
    for(int i = 0; i < n; i++)
        arr[i] = (rand() % n) + 1;
}

void generate_sorted(int arr[], int n){
    for(int i = 0; i < n; i++)
        arr[i] = i;
}

void generate_reverse(int arr[], int n){
    for(int i = 0; i < n; i++)
        arr[i] = n - i;
}

void generate_duplicates(int arr[], int n){
    for(int i = 0; i < n; i++)
        arr[i] = (rand() % 20) + 1;
}

void generate_nearly_sorted(int arr[], int n){
    generate_sorted(arr, n);

    int swaps = n / 20;   // 5%
    for(int i = 0; i < swaps; i++){
        int a = rand() % n;
        int b = rand() % n;
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }
}


void merge(int arr[], int low, int high, int mid, Metrics *m){
    int temp[high-low+1];

    int i = low;
    int j = mid+1;
    int k = 0;

    while(i <= mid && j <= high){
        m -> comparisons++;
        if (arr[i] <= arr[j]){
            temp[k++] = arr[i++];
        } else {
            temp[k++] = arr[j++]; 
        }
        m -> writes++;
    }

    // j side is done, only i side left
    while(i <= mid){
        temp[k++] = arr[i++];
        m -> writes++;
    }

    // i side done now, only j left
    while(j <= high){
        temp[k++] = arr[j++];
        m -> writes++;
    }

    // copy back from the temp array
    for(i = low, k = 0; i<=high; i++, k++){
        arr[i] = temp[k];
        m -> writes++;
    }
}

void merge_sort(int arr[], int low, int high, Metrics *m){

    if (low >= high){
        return;
    }

    int mid = low+((high - low)/2);

    merge_sort(arr, low, mid, m);
    merge_sort(arr, mid+1, high, m);

    merge(arr, low, high, mid, m);
    


}

int main(){

    srand(time(NULL));
    int trials = 20;
    double total_time = 0;
    long total_comp = 0;
    long total_writes = 0;

    int size = 20000;

    for (int i = 0; i<trials; i++){
        Metrics m;
        m.comparisons = 0;
        m.writes = 0;
        
        int arr[size];

        generate_sorted(arr, size);


        clock_t start, end;
        double t;

        start = clock(); // timing it
        merge_sort(arr, 0, size-1, &m);
        end = clock(); // close time it

        t = ((double)(end-start))/CLOCKS_PER_SEC;

        total_comp += m.comparisons;
        total_writes += m.writes;
        total_time += t;
    }

    printf("\nAverage for %d\nComparisons: %ld\nWrites: %ld\nRun Time: %f\n", size, total_comp/20, total_writes/20, (total_time/20)*1000);

    
    
}