/* Shell sort
 * Best: n. Worst: n^(3/2). Average: depends or n(lgn)^2
 * Memorey: 1. Stable: No. Method: Insertion.
 * Suitable for arrays that almost sorted and not too large
 * Author: creasy, April 24, 2011.
 * Reference: http://en.wikipedia.org/wiki/Shell_sort
 * http://www.sorting-algorithms.com/shell-sort
 */
#include<limits.h>
#include<stdio.h>
#include<stdlib.h>
#include<time.h>
//#define exch(a,b,c)	c=a;a=b;b=c;
//#define REVEAL 1

void insertSortStep(float *input, int begin, int end, int step){
	int i, j;
	float key;
	for(i=begin; i<=end; i+=step){
		key=input[i];
		j=i-step;
		while(j>=begin && input[j]>key){
			input[j+step]=input[j];
			j-=step;
		}
		input[j+step]=key;
	}
}

void shellSort(float *input, int begin, int end){
	int factor=3;
	int devide=1;
	int length=end-begin+1;
	int i;
	while(devide<length)
		devide=devide*factor+1;
	for(;devide>0;devide=devide/3){
		for(i=0; i<devide; i++)
			insertSortStep(input, i, end, devide);
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
		input[i]=(float)(rand()%length);
#ifdef REVEAL
	printf("length=%d\n", length);
	printf("Before the sorting:\n");
	for(i=0; i<length;i++)
		printf("%f ", input[i]);
	printf("\n");
#endif

	shellSort(input,0, length-1);

#ifdef REVEAL
	printf("After the sorting:\n");
	for(i=0;i<length;i++)
		printf("%f ", input[i]);
	printf("\n");
#endif
	return 0;
}

