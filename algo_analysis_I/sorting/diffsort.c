#include<stdio.h>
#include<time.h>
#include<stdlib.h>
#include<math.h>

void InsertSort(int *Array, int size);
void BubbleSort(int *Array, int size);

// determin if the ith node need to move within the heap
void MaxHeapify(int *Array, int i, int size){
	int temp;
	int l = i*2;	// left child
	int r = i*2+1;	// right child
	int largest;
	if (l<size && Array[l]>Array[i])
		largest = l;
	else
		largest = i;
	if (r<size && Array[r]>Array[largest])
		largest = r;
	if (largest!=i){		// the ith item needs to move
		temp = Array[i];
		Array[i] = Array[largest];
		Array[largest] = temp;
		MaxHeapify(Array, largest, size);	// recursively call itself
	}
}
// build the max-heap
void BuildHeap(int *Array, int size){
	int i;
	for(i=(size/2+1);i>=0;i--)
		MaxHeapify(Array, i, size);
}
// now finally~ the heap sorting algorithm
void HeapSort(int *Array, int size){
	BuildHeap(Array, size);
	int SortingSize = size-1;
	int temp;
	int i;
	for(i=size-1; i>0; i--){
		temp = Array[i];
		Array[i] = Array[0];
		Array[0] = temp;
		MaxHeapify(Array, 0, SortingSize);
		SortingSize--;
	}
}

//**********************
// partition for the random quick sorting
int Partition (int *Array, int lower, int upper){
	int LowerIndex = lower;
	int temp;
	int j;
	for (j = lower; j<upper; j++){
		if (Array[j]<=Array[upper]){
			temp = Array[j];
			Array[j] = Array[LowerIndex];
			Array[LowerIndex] = temp;
			LowerIndex++;
		}
	}
	temp = Array[LowerIndex];
	Array[LowerIndex] = Array[upper];
	Array[upper] = temp;
	return LowerIndex;
}

// Random Quick Sorting algorithm
void RandomQuickSort(int *Array, int lower, int upper){
	int i;
	if (lower < upper){
		// first generate the random partition
		//srand(time(NULL));
		//int r = rand()%(upper-lower+1)+lower;		// generate random value within [lower, upper]
		//printf("lower=%d, upper=%d, the segmentation r=%d.\n", lower, upper, r);
		//int temp = Array[upper];
		//Array[upper] = Array[r];
		//Array[r] = temp;		// randomly pick the partition reference
		int q = Partition(Array, lower, upper);
		printf("lower=%d, upper=%d, the partition result is q=%d.\n",lower, upper, q);
		printf("In this loop, the array is:\n");
		for (i=0;i<10;i++)
			printf("%d, ", Array[i]);
		printf("\n");

		// then, sort recursively
		RandomQuickSort(Array, lower, q-1);
		RandomQuickSort(Array, q+1, upper);
	}
}

//**********************
int main(){
	int size=10;
	int randNum[size];
	int i;
	srand(time(NULL));

	printf("the original generated numbers are:\n");
	for (i=0; i<size;i++){
		randNum[i] = rand()%100+1;		// generate number in [1,100]
		printf("%d, ", randNum[i]);
	}
	printf("\n");
	printf("The size of the array is %lu.\n", sizeof(randNum) );

	//InsertSort(randNum, size);
	//BubbleSort(randNum,size);
	HeapSort(randNum, size);
	//RandomQuickSort(randNum, 0, size-1);	// the input variables are a little bit tricky...:P

	printf("After sorting the sequence is:\n");
	for (i=0; i<size;i++)
		printf("%d, ", randNum[i]);
	printf("\n");
	return 0;
}

void InsertSort(int *Array, int size){
	// sort the array in increasing order
	int i,j;
	int key;
	for (j=1; j<size; j++){
		key = Array[j];
		i = j-1;
		while (i>=0 && Array[i]>key){
			Array[i+1]=Array[i];
			i--;
		}
		Array[i+1]=key;
	}
}

void BubbleSort(int *Array, int size){
	int i, j, temp;
	for (i=0; i<size; i++){
		for (j=size-1;j>i;j--){
			if (Array[j]<Array[j-1]){
				temp = Array[j];
				Array[j]=Array[j-1];
				Array[j-1]=temp;
			}
		}
	}
}
