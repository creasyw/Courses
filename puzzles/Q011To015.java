import java.util.*;
import java.lang.*;
import java.io.*;


public class Q011To015
{
	int q011;

	public Q011To015()
	{
		q011 = question11();
	}

	// What is the greatest product of four adjacent numbers in any direction
	// (up, down, left, right, or diagonally) in the 20×20 grid (input file Q11.data)?
	// FOR READING FILE, the reading sequence is file-->buffer (read line by line)
	// -->ArrayList (read token by token)-->Integer Array (with checking)
	// The array convertion is done in question11() to avoid global variables.
	private List<List<Integer>> readFile()
	{
		List<List<Integer>> list = new ArrayList<List<Integer>>();
		try
		{
			File file = new File("Q11.data");
			FileReader reader = new FileReader(file);
			BufferedReader in = new BufferedReader(reader);
			String string;
			while((string=in.readLine())!=null)
			{
				Scanner scanner = new Scanner(string);
				List<Integer> templist = new ArrayList<Integer>();
				while(scanner.hasNextInt())
				{
					templist.add(scanner.nextInt());
				}
				list.add(templist);
			}

		}
		catch(IOException ioe)
		{
			System.out.println("Exception while reading the file: "+ioe);
		}
		return list;
	}
	private int question11()
	{
		List<List<Integer>> list = new ArrayList<List<Integer>>();
		list = readFile();
		int column = list.get(0).size();
		int row = list.size();
		Integer data[][] = new Integer[row][column];

		// convert ArrayList to array to facilitate random access
		for(int i=0; i<row; i++)
		{
			if(column!=list.get(i).size())
			{
				System.out.println("The length of array in input file is irregular..\n");
				return 0;
			}
			data[i] = list.get(i).toArray(new Integer[column]);
		}
		
		// calculate the production in FOUR directions:
		// down, right, right-down, AND left-down
		int product = 0;
		int temp;
		boolean rowflag = false, columnflag = false;
		for(int i=0;i<row;i++)
		{
			for(int j=0;j<column;j++)
			{
				if(i+3<row)
				{
					temp=data[i][j]*data[i+1][j]*data[i+2][j]*data[i+3][j];
					rowflag=true;
					product = Math.max(product,temp);
				}
				if(j+3<column)
				{
					temp=data[i][j]*data[i][j+1]*data[i][j+2]*data[i][j+3];
					columnflag=true;
					product = Math.max(product,temp);
				}
				if(rowflag && columnflag)
				{
					temp=data[i][j]*data[i+1][j+1]*data[i+2][j+2]*data[i+3][j+3];
					product = Math.max(product,temp);
				}
				if(i+3<row && j-3>=0)
				{
					temp=data[i][j]*data[i+1][j-1]*data[i+2][j-2]*data[i+3][j-3];
					product = Math.max(product,temp);
				}
				rowflag=columnflag=false;
			}
		}
		return product;
	}


	public static void main (String args[])
	{
		Q011To015 question = new Q011To015();
		System.out.printf("Q011: result = %d.\n", question.q011);
	}
}


