/* This piece of code implements the binary heap for sorting
 * Reference: Introduction of Algorithms (CLRS)
 * Author: Qiong Wu, April 22, 2011
 * Quoted from the CLRS: "Heapsort is an excellent algorithm, but
 * a good implementation of quicksort, usually beats it in practice."
 *
 * Heap sort:
 * Best: nlgn. Worst: nlgn. Average: nlgn.
 * Stable: NO. Memory: 1. Method: selection.
 * However, assuming the sorting operated object is a C array,
 * to add the heap relation, the memory requirement is also linear.
 */
#include<limits.h>
#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#define exch(a,b,c)	c=a;a=b;b=c;
//#define REVEAL 1
// determin if the ith node need to move within the heap
void maxHeapify(float *input, int i, int heapsize){
	float temp;
	int l = i*2;	// left child
	int r = i*2+1;	// right child
	int largest;
	//printf("enter heapify\n");
	if (l<heapsize && input[l]>input[i])
		largest = l;
	else
		largest = i;
	if (r<heapsize && input[r]>input[largest])
		largest = r;
	if (largest!=i){		// the ith item needs to move
		exch(input[i],input[largest],temp);
		maxHeapify(input, largest, heapsize);	// recursively call itself
	}
}


/* Build the heap
 * Input-- input array and the length of the array
 * Upper boundary for computation O(n) (linear).
 */
void buildMaxHeap(float *input, int length){
	int i;
	// arrange the heap
	for(i=length/2+1; i>=0; i--)
		maxHeapify(input,i,length);
}

// Heap sorting
void heapSort(float *input, int length){
	int i;
	int heapsize=length;
	float temp;
	if(input==NULL || length<0){
		printf("the input values for building heap is invalid\n");
		return;
	}
	buildMaxHeap(input, length);
	for(i=length-1; i>0; i--){
		exch(input[i], input[0], temp);
		heapsize--;
		maxHeapify(input,0,heapsize);
	}
}


//-- main function
int main(int argc, char *argv[]){
	FILE *fp;
	float *input;
	int length;
	int i;
	if(argc!=2){
		printf("The input format should be <command> <input length>\n");
		return 1;
	}
	if((length=atoi(argv[1]))<=0){
		printf("Invalid length input! (must be >0)\n");
		return 1;
	}
	input=(float *)malloc(length*sizeof(float));
	srand(time(NULL));
	for(i=0; i<length; i++)
		input[i]=(float)(rand()/length);
#ifdef REVEAL
	printf("length=%d\n", length);
	printf("Before the sorting:\n");
	for(i=0; i<length;i++)
		printf("%f ", input[i]);
	printf("\n");
#endif

	heapSort(input,length);

#ifdef REVEAL
	printf("After the sorting:\n");
	for(i=0;i<length;i++)
		printf("%f ", input[i]);
	printf("\n");
#endif
	return 0;
}
