#include<stdio.h>
#include<limits.h>
#include<time.h>

int main(int argc, char *argv[]){
	FILE *fp;
	int length;
	int i;
	srand(time(NULL));

	if(argc!=3){
		printf("The input format should be <command> <input>\n");
		return 1;
	}
	if((length=atoi(argv[1]))<=0){
		printf("the number is invalid.\n");
		return 1;
	}
	if((fp=fopen(argv[2],"w"))==NULL){
		printf("Cannot open the input file %s\n", argv[2]);
		return 1;
	}
	fprintf(fp, "%d\n", length);
	for(i=0;i<length;i++)
		fprintf(fp, "%d\t", rand()%1000);
	fclose(fp);
}
