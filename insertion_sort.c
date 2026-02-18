#include <stdio.h>

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
    int arr[] = {5, 6, 7, 2, 3, 1, 4, 7, 9, 11};

    int size = sizeof(arr)/sizeof(arr[0]);
    Metrics m = insertionSort(arr, size);
    printf("Comparisons: %ld\nShifts: %ld\n", m.comparisons, m.shifts);

}