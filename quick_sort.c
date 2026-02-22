#include <stdio.h>


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

void quick_sort(int arr[], int low, int high){

    // base case
    if (low >= high){
        return;
    }

    // lomuto partition
    int i = low - 1;
    int pivot = arr[high]; // last element of the array

    for (int j = low; j<high; j++){
        if (arr[j] <= pivot){
            i++;
            int temp = arr[j];
            arr[j] = arr[i];
            arr[i] = temp;
        }

    }
    i++;
    int temp = arr[i];
    arr[i] = arr[high];
    arr[high] = temp;
    


    quick_sort(arr, i+1, high);
    quick_sort(arr, low, i-1);



}

int main(){

    int arr[] = {5,6,1,5,9,2,4};
    int size = sizeof(arr)/sizeof(arr[0]);

    quick_sort(arr, 0, size-1);
    for (int i =0; i<size; i++){
        printf(" %d", arr[i]);
    }

}