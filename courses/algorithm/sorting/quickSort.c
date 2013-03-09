/* Quicksort:
 * Reference: CLRS. "Quicksort is often the best practical choice, 
 * because it is remarkably efficient on the average and the constant
 * factors hidden are quite small. It also sorts in place and works 
 * well even in virtual-memory environments."
 * Author: creasy, April 22, 2011.
 * Best: nlgn, Worst: n^2, Average: nlgn.
 * Memeroy: lgn. Stable: depends. Method: partitioning
 */
#include<limits.h>
#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#define exch(a,b,c)	c=a;a=b;b=c;
//#define REVEAL 1
//#define RANDOMSORT 1

void quickSort(float *input, int begin, int end){
	int mid;
	if(begin<end){
		mid=partition(input, begin, end);
		quickSort(input, begin, mid-1);
		quickSort(input, mid+1, end);
	}
	return;
}

int partition(float *input, int begin, int end){
	float bmark, temp;
	int i, j;
	float *op, *sorted;
#ifdef RANDOMSORT
	j=(rand()%(end-begin+1)+begin);		// set srand(time(NULL)) in main function
	temp=input[j];
	input[j]=input[end];
	input[end]=temp;
#endif
	bmark=input[end];
	sorted=op=&(input[begin]);
	for(j=begin; j<end; j++){
		if(*(op)<=bmark){
			temp=*(sorted);
			*(sorted)=*(op);
			*(op)=temp;
			sorted++;
		}
		op++;
	}
	temp=*(sorted);
	*(sorted)=input[end];
	input[end]=temp;
	return begin+(sorted-&(input[begin]));
}

/* The 3-way partition variation of quick sort has slightly higher overhead
 * compared to the standard 2-way partition version. Both have the same best,
 * typical, and worst case time bounds, but this version is highly adaptive in
 * the very common case of sorting with few unique key.
 * Reference: Robert Sedgewick,
 * http://www.sorting-algorithms.com/static/QuicksortIsOptimal.pdf
 */

void quickSort3(float *input, int begin, int end){
	float temp;
	float *vpr, *ipr, *epr;
	float *ppr, *qpr;
	ipr=ppr=(&(input[begin]))-1;
	vpr=qpr=epr=&(input[end]);
	if (end<=begin)
		return;
	//printf("looping...\n");
	for(;;){
		while(*(++ipr)<*(vpr));
			//ipr++;
		while(*(vpr)<*(--epr))
			if(epr==&(input[begin]))
				break;
		if(ipr>=epr)
			break;
		exch(*(ipr),*(epr),temp);
		if(*(ipr)==*(vpr)){
			ppr++;
			exch(*(ppr),*(ipr),temp);
			//ppr++;
		}
		if(*(vpr)==*(epr)){
			qpr--;
			exch(*(epr),*(qpr),temp);
		}
	}
	//printf("rearranging...\n");
	//ppr--;
	exch(*(ipr),*(vpr),temp);
	epr=ipr-1;
	ipr++;
	vpr=&(input[begin]);
	//printf("changing...1st\n");
	while(vpr<ppr){
		exch(*(vpr),*(epr),temp);
		vpr++;
		epr--;
	}
	vpr=(&(input[end]));
	vpr--;
	//printf("changing...2nd\n");
	while(vpr>qpr){
		exch(*(vpr),*(ipr),temp);
		vpr--;
		ipr++;
	}
	quickSort3(input, begin, epr-input);
	quickSort3(input, ipr-input, end);
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

	//quickSort(input,0,length-1);
	quickSort3(input,0,length-1);

#ifdef REVEAL
	printf("After the sorting:\n");
	for(i=0;i<length;i++)
		printf("%f ", input[i]);
	printf("\n");
#endif
	return 0;
}

