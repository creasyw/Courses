import java.util.*;
import java.lang.*;
import java.io.*;

public class Q016To020
{
	int q016;

	public Q016To020()
	{
		q016 = question016();
	}

	// 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
	// What is the sum of the digits of the number 21000?
	// The most elegant solution is from StackOverflow
	// http://stackoverflow.com/questions/377361/sum-of-the-digits-of-the-number-21000
	private int question016()
	{
		int sum = 0;
		for( char c: java.math.BigInteger.valueOf(2).pow(1000).toString().toCharArray())
		{
			sum += c-48;	// ascii to its integer value
		}
		return sum;
	}


	public static void main(String args[])
	{
		Q016To020 result = new Q016To020();
		System.out.printf("qeustion16: result = %d.\n",result.q016);
	}
}

