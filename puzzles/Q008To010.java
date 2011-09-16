import java.util.*;
import java.lang.*;

public class Q008To010
{
	long result;
	// for Q9 to store all of the facotors
	static List<Integer> list = new ArrayList<Integer>();

	public Q008To010()
	{
		result = question10();
	}
	// Find the greatest product of five consecutive digits in the given 1000-digit number.
	private int question8()
	{
		String input = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450";
		int product = 1;
		int temp = 1;
		int divisor;
		int count = 0;
		for(char item : input.toCharArray())
		{
			if(count>=5)
			{
				divisor = Character.getNumericValue(input.charAt(count-5));
				if(divisor!=0)
					temp=temp/divisor;
				else {
					temp = 1;
					for(int i=1;i<5;i++)
						temp=temp*Character.getNumericValue(input.charAt(count+i-5));
				}
			}
			temp = temp*Character.getNumericValue(item);
			if(count>=5 && temp>product)
				product=temp;
			count++;
		}
		return product;
	}

	// A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
	// a^2+b^2=c^2. For the exactly one Pythagorean triplet satisfying a+b+c=1000. Find abc.
	// SOLUTION: From http://en.wikipedia.org/wiki/Pythagorean_triple,
	// the basic way to generate Pythagorean triples is to use Euclid's formular:
	// a=m^2-n^2, b=2mn, c=m^2+n^2, where m>n.
	// a+b+c=1000 ==> m(m+n)=500 & m>0, n>0, m>n
	// This function perform the basic factorization and store the results in a ArrayList.
	private void factorization(int val)
	{
		//static ArrayList<int> list = new ArrayList<int>;
		for(int i=2; i<=val/i; i++)
		{
			while(val%i==0)
			{
				list.add(i);
				val= val/i;
			}
		}
		if(val>1)
			list.add(val);
	}
	// Find a and b from factorization (val=a*b) with certain criteria to solve the problem
	// In this case, they are "a<b" and "a>b/2".
	private int[] findFactors(int val)
	{
		int length = list.size();
		int i, j;
		int a, b, temp;
		int[] result = {0,0};
		boolean flag = false;

		if(val==0)
			return result;
		for(i=0;i<=length-2;i++)
		{
			for(j=1;j<=length-1;j++)
			{
				a=list.get(i).intValue()*list.get(j).intValue();
				b=val/a;
				if(a>b)
				{
					temp=a;
					a=b;
					b=temp;
				}
				if(a>b/2)
				{
					result[0]=a;
					result[1]=b;
					return result;
				}
			}
		}
		return result;
	}

	private int question9()
	{
		factorization(500);
		int[] factors=findFactors(500);
		int a ,b;
		if(factors[0]==0)
		{
			System.out.println("There is something wrong with factorization.");
			return 0;
		}
		a = factors[0];
		b =factors[1]-a;
		return (int)(Math.pow(a,2)-Math.pow(b,2))*(2*a*b)*(int)(Math.pow(a,2)+Math.pow(b,2));
	}

	// The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
	// Find the sum of all the primes below two million.
	// SOLUTION: The idea is repeated as Q1: testing all primes from 2 to sqrt(n) to see if n is a prime.
	// The only tricky part is the range of "sum". The range of int is (-2,147,483,648,2,147,483,648)
	// which make "sum" out of range. Changing it to "long" should be fine.
	private long question10()
	{
		int THRESHOLD = 2000000;
		ArrayList<Integer> prime = new ArrayList<Integer>();
		long sum = 2;
		boolean flag = true;

		prime.add(2);
		for(int i=3; i<THRESHOLD; i++)
		{
			Iterator<Integer> iter = prime.iterator();
			int j = iter.next().intValue();
			while(j<=Math.sqrt(i))
			{
				if(i%j==0)
				{
					flag = false;
					break;
				}
				if(iter.hasNext())
					j = iter.next().intValue();
				else
					break;
			}
			if(flag)
			{
				prime.add(i);
				sum +=i;
			}
			else
				flag = true;
		}
		return sum;
	}


	public static void main (String args[])
	{
		Q008To010 question = new Q008To010();
		System.out.printf("result = %d.\n",question.result);
	}

}





