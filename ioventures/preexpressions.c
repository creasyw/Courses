#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

#define BUFSIZE 2048

struct node{
	double val;
	char op;
	struct node *p, *lc, *rc;
};


int calculate(struct node *n);
int calPreExpression(char *buff, struct node* root);


int main(int argc, char *argv[]){
	FILE *fp;
	char buff[BUFSIZE];
	int check, line;
	struct node *root;

	if(argc!=2){
		printf("The input format should be ./preexpression INPUT_FILE.\n");
		return 1;
	}
	if((fp=fopen(argv[1], "r")) == NULL){
		printf("The input file cannot open.");
		return 1;
	}
	line = 1;
	root = (struct node*)malloc(sizeof(struct node));
	// read the file line by line
	while(fgets(buff, sizeof(buff), fp)!=NULL){
		check = calPreExpression(buff, root);
		if(check==0){
			printf("The prefix expression in LINE %d is invalid!\n", line);
		} else {
			printf("The result of prefix expression in LINE %d is %f.\n", line, root->val);
		}
		line++;
	}

	fclose(fp);
	return 0;
}


// calculate the inner expression with two operands and one operator
// return o for exception and 1 for success
int calculate(struct node *n){
	int a = n->lc->val;
	int b = n->rc->val;

	switch(n->op){
		case '+':
			n->val = a+b;
			break;
		case '-':
			n->val = a-b;
			break;
		case '*':
			n->val = a*b;
			break;
		case '/':
			if(b==0)  return 0;
			n->val = a/b;
			break;
		default:
			return 0;
	}
	return 1;
}

// calculate the prefix expression for each line
// return o for exception and 1 for success
int calPreExpression(char *buff, struct node* root){
	char *pt, *npt;
	struct node *iter;
	int check;
	int flag=0;

	pt = &(buff[0]);
	while(*pt!='\0'){
		if(isspace(*pt)){	// jump to next valid input char
			pt++;
			continue;
		}
		// build the root of the binary tree
		if(flag==0){
			// only suppose "+,-,*,/" as valid operators
			if(*pt!='+' && *pt!='-' && *pt!='*' && *pt!='/'){
				printf("The beginning of the input might be invalid. Please check.\n");
				return 0;
			}
			root->op=*pt;
			iter=root;
			pt++;
			flag = 1;
			root->lc = root->rc = root->p = NULL;
		}
		else{
			struct node *new;
			new=(struct node*)malloc(sizeof(struct node));
			new->p = iter;
			new->lc = new->rc = NULL;
			// check first if new operator should be added
			if(*pt=='+'||*pt=='-'||*pt=='*'||*pt=='/'){
				if(iter->lc==NULL){
					iter->lc = new;
				} else{
					iter->rc = new;
				}
				iter=new;
				new->op = *pt;
				pt++;
			} else {	// then add operand
				new->val = strtod(pt, &(npt));
				// if there is no operator nor operand extracted,
				// something must be wrong.
				if(pt==npt){
					printf("There is some invalid input: %s", pt);
					return 0;
				}
				if(iter->lc==NULL){
					iter->lc = new;
				} else {
					iter->rc = new;
					// after adding new operand in right hand side,
					// at least one triangle formular with operator in the "iter"
					// and two operands in the lower nodes can be calculated.
					while(iter!=NULL && iter->rc!=NULL){
						check = calculate(iter);
						if(check==0){
							printf("The prefix expression is invalid!\n");
							return 0;
						}
						iter = iter->p;
					}
				}
				pt = npt;
			}
		}
		if(iter==NULL)
			break;
	}
	// further check if the prefix expression is valid.
	// the "while" loop above only calculate the longest valid prefix expression.
	// if there is some thing left in the same line, there should be something wrong.
	if(strlen(pt)!=1){
		printf("There is something wrong with input section: %s", pt);
		return 0;
	}
	return 1;
}

