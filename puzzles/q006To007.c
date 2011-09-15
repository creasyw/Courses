#include<stdio.h>
#include<stdlib.h>
#include<math.h>

// Hence the difference between the sum of the squares of the first
// ten natural numbers and the square of the sum is 3025 − 385 = 2640.
// Find the difference between the sum of the squares of the first
// one hundred natural numbers and the square of the sum.
// SOLUTION: This can be solved with the formula that calculate the sum of
// consecutive natural sequence: 1^2+2^2+...+n^2=n(n+1)(2n+1)/6, and
// the sum of consecutive natural numbers: 1+2+...+n=(n+1)n/2
int question6()
{
	int n = 100;
	int sum1, sum2;
	
	sum1 = pow(n*(n+1)/2, 2);
	sum2 = n*(n+1)*(2*n+1)/6;
	return sum1-sum2;
}

// By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
// we can see that the 6th prime is 13.
// What is the 10001st prime number?
// SOLUTION: it is the simpler version of Q4
int question7()
{
	int count = 6;
	int n=17;
	int i;
	int flag=0;

	while(count!=10001)
	{
		for(i=2;i<=floor(sqrt(n));i++)
		{
			if(n%i==0)
			{
				flag=1;
				break;
			}
		}
		if(flag)
			flag=0;
		else{
			count++;
		}
		n+=2;
	}
	return n-2;	// the last round add 2 more to the final result
}

		
int main()
{
	printf("result = %d\n", question7());
	return 0;
}


