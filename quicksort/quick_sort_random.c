#include <stdio.h>
#include <time.h>
#include <stdlib.h>


typedef struct{
    long comparisons;
    long swaps;
} Metrics;

/*ARRAY GENERATOR*/
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

/* MAIN CODE: QUICK SORT */

void quick_sort(int arr[], int low, int high, Metrics *m){

    // base case
    if (low >= high){
        return;
    }

    // lomuto partition
    int i = low - 1;

    int ri = low + rand()%(high-low + 1);
    
    // move random pivot to end
    int temp = arr[ri];
    arr[ri] = arr[high];
    arr[high] = temp; // random taken to highest point / last element
    m->swaps++;

    int pivot = arr[high]; // last element of the array (random)

    for (int j = low; j<high; j++){
        m -> comparisons++;
        if (arr[j] <= pivot){
            m -> swaps++;
            i++;
            int temp = arr[j];
            arr[j] = arr[i];
            arr[i] = temp;
        }

    }
    m -> swaps++; // counting swaps
    i++;
    temp = arr[i];
    arr[i] = arr[high];
    arr[high] = temp;
    


    quick_sort(arr, i+1, high, m);
    quick_sort(arr, low, i-1, m);



}

int main(){

    srand(time(NULL));
    int trials = 20;
    double total_time = 0;
    long total_comp = 0;
    long total_swaps = 0;

    int size = 50000;

    for (int i = 0; i<trials; i++){
        Metrics m;
        m.comparisons = 0;
        m.swaps = 0;
        
        int arr[size];
        generate_nearly_sorted(arr, size);

        clock_t start, end;
        double t;

        start = clock(); // timing it
        quick_sort(arr, 0, size-1, &m);
        end = clock(); // close time it

        t = ((double)(end-start))/CLOCKS_PER_SEC;

        total_comp += m.comparisons;
        total_swaps += m.swaps;
        total_time += t;
    }

    printf("\nAverage for %d\nComparisons: %ld\nSwaps: %ld\nRun Time: %f\n", size, total_comp/20, total_swaps/20, (total_time/20)*1000);

    

}
