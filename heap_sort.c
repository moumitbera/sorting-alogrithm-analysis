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


void make_heap(int arr[], int n, int i, Metrics *m){

    int largest = i;
    int left_node = 2*i +1;
    int right_node = 2*i + 2;

    if (left_node<n){
        m->comparisons++;
        if (arr[left_node] > arr[largest]){
            largest = left_node;
        }
    }

    if(right_node<n){
        m->comparisons++;
        if(arr[right_node]>arr[largest]){
            largest = right_node;
        }
    }

    // the parent / root is not the largest
    if(largest != i){
        m->swaps++;

        int temp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = temp;

        make_heap(arr, n, largest, m);
    }

}

void heap_sort(int arr[], int n, Metrics *m){
    // max heaps
    for(int i = n/2-1; i>= 0; i--){
        make_heap(arr, n, i, m);
    }

    // extract
    for(int i = n-1; i>0; i--){
        m->swaps++;

        int temp = arr[0];
        arr[0] = arr[i];
        arr[i] = temp;

        make_heap(arr, i, 0, m);
    }
}

int main(){

    srand(time(NULL));

    int trials = 20;
    int size = 1000;

    long total_comp = 0;
    long total_swaps = 0;
    double total_time = 0;

    for(int t = 0; t < trials; t++){

        Metrics m;
        m.comparisons = 0;
        m.swaps = 0;

        int arr[size];

        // Change generator here for testing:
        // generate_sorted(arr, size);
        // generate_reverse(arr, size);
        // generate_random(arr, size);
        // generate_duplicates(arr, size);
        generate_nearly_sorted(arr, size);

        clock_t start = clock();
        heap_sort(arr, size, &m);
        clock_t end = clock();

        double runtime = ((double)(end - start)) / CLOCKS_PER_SEC;

        total_comp += m.comparisons;
        total_swaps += m.swaps;
        total_time += runtime;
    }

    printf("\nAverage for n = %d\n", size);
    printf("Comparisons: %ld\n", total_comp / trials);
    printf("Swaps: %ld\n", total_swaps / trials);
    printf("Run Time (ms): %f\n", (total_time / trials) * 1000);

    return 0;
}