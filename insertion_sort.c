#include <stdio.h>
#include <time.h>
#include <stdlib.h>

typedef struct{
    long comparisons;
    long shifts;
} Metrics;

Metrics insertionSort(int arr[], int size) {

    Metrics mat;
    mat.comparisons = 0;
    mat.shifts = 0;

    for(int i = 1; i<size; i++){

        int curr = arr[i];
        int j = i-1; //looking back index


        while(j>=0){
            mat.comparisons++; // counting each comparisons
            if (arr[j] > curr){
                mat.shifts++;
                arr[j+1] = arr[j]; // move every other element to the right
                j--;
            } else {
                break; // to exit out in case it's sorted
            }
            
        }

        arr[j+1] = curr; // insert the element back

    }

    return mat;


    /* PRINTING ARRAY: */
    // printf("Sorted Array: [");
    // for (int i = 0; i<size; i++){
    //     printf(" %d ", arr[i]);
    // }
    // printf("] \n");

}


int main(){

    int trials = 20;
    double total_time = 0;
    long total_comp = 0;
    long total_shifts = 0;
    
    srand(time(NULL));
    int n = 50000;  
    for (int k = 0; k<trials; k++){


        
        int arr[n];

        clock_t start, end;
        double t;

        
        // /*AVG CASE: RANDOM ELEMENTS*/
        // for (int i = 0; i<n; i++){
        //     arr[i] = (rand()%n)+1;
        // }

        // /*BEST CASE: WHEN ALREADY SORTED (ASCENDING)*/
        // for (int i = 0; i<n; i++){
        //     arr[i] = i;
        // }

        // /*WORST CASE: WHEN SORTED DECENDING*/
        // for (int j = 0,i = n; j<n && i>0; j++,i--){
        //     arr[j] = i;
        // }

        // /*DUPLICATE HEAVY CASE*/
        // for (int i = 0; i<n; i++){
        //     arr[i] = (rand()%20)+1;
        // }

        /*NEARLY SORTED*/
        for (int i = 0; i<n; i++){
            arr[i] = i;
        } // sorted array
        int swaps = n/20; //(5% swaps);
        for (int i = 0; i<swaps; i++){
            int a = rand() % n;
            int b = rand() % n;
            int temp = arr[a];
            arr[a] = arr[b];
            arr[b] = temp;
        } // 5% randomly changed




        int size = sizeof(arr)/sizeof(arr[0]); // = n

        start = clock(); // timing it
        Metrics m = insertionSort(arr, size);
        end = clock(); // close time it

        t = ((double)(end-start))/CLOCKS_PER_SEC;

        total_comp += m.comparisons;
        total_shifts += m.shifts;
        total_time += t;

        

    }

    printf("\nAverage for %d\nComparisons: %ld\nShifts: %ld\nRun Time: %f\n", n, total_comp/20, total_shifts/20, total_time/20);

    
}
