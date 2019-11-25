
#include <bits/stdc++.h>
#include <stdlib.h>
#include <stdio.h>

using namespace std;


void swap(int *val1,int *val2){
	int temp = *val1;
	*val1 = *val2;
	*val2 = temp;
}
//void InsertionSort(int list[],int n);
void InsertionSort(int list[],int n){
	
	int i,j,k;
	for(i=1;i<n;i++){
		k = list[i];
		j = i-1;
		while(j>=0 && list[j]>k){
			list[j+1] = list[j];
			j= j-1;
		}
		list[j+1] = k;
	}
	
}
void selectionSort(int list[],int n){
	int i,j,min;
	for(i=0;i<n-1;i++){
		min = i;
		for(j=i+1;j<n;j++){
			if(list[j]<list[min])
				min = j;
			
		}
		swap(&list[min],&list[i]);
	}
}

void merge(int arr[], int l, int m, int r) 
{ 
    int i, j, k; 
    int n1 = m - l + 1; 
    int n2 =  r - m; 
    
    int L[n1], R[n2]; 
  
    for (i = 0; i < n1; i++) 
        L[i] = arr[l + i]; 
    for (j = 0; j < n2; j++) 
        R[j] = arr[m + 1+ j]; 
  
    i = 0; 
    j = 0; 
    k = l; 
    while (i < n1 && j < n2) 
    { 
        if (L[i] <= R[j]) 
        { 
            arr[k] = L[i]; 
            i++; 
        } 
        else
        { 
            arr[k] = R[j]; 
            j++; 
        } 
        k++; 
    } 
  
    while (i < n1) 
    { 
        arr[k] = L[i]; 
        i++; 
        k++; 
    } 
  
    while (j < n2) 
    { 
        arr[k] = R[j]; 
        j++; 
        k++; 
    } 
} 
  
void mergeSort(int arr[], int l, int r) 
{ 
    if (l < r) 
    { 
        
        int m = l+(r-l)/2; 
  
        mergeSort(arr, l, m); 
        mergeSort(arr, m+1, r); 
  
        merge(arr, l, m, r); 
    } 
} 
int partition (int arr[], int low, int high)  
{  
    int pivot = arr[high];   
    int i = (low - 1); 
  
    for (int j = low; j <= high - 1; j++)  
    {  
        
        if (arr[j] < pivot)  
        {  
            i++; 
            swap(&arr[i], &arr[j]);  
        }  
    }  
    swap(&arr[i + 1], &arr[high]);  
    return (i + 1);  
}  
  

void quickSort(int arr[], int low, int high)  
{  
    if (low < high)  
    {  
    
        int pi = partition(arr, low, high);  

        quickSort(arr, low, pi - 1);  
        quickSort(arr, pi + 1, high);  
    }  
}  
  

int main() {
    int list[10]={2389,5,62,1,4,3,11,6,33};
    //srand(unsigned)(time(NULL));
    printf("The List before Sorting\n");
    for (int j = 0; j < 10; ++j) {
       // list[j]= rand()%10000;
        printf("%d \t",list[j]);
    }
    int n = sizeof(list)/sizeof(list[0]);
    
    printf("\n");
    

//  InsertionSort(list,n);
//	selectionSort(list,n);
//	mergeSort(list,0,n-1);
//	quickSort(list,0,n-1);
    
    printf("The List after Sorting\n");
    for (int j = 0; j < 10; ++j) {
//        list[j]= rand()%10000;
        printf("%d \t",list[j]);
    }

    return 0;
}




