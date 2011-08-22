import java.util.Arrays;
import java.util.Scanner;

public class UsingArrays{
	private int intArray[] = new int [10];
	private int intArrayCopy[];

	public UsingArrays(){
		intArrayCopy = new int [intArray.length];
		Scanner input = new Scanner(System.in);
		System.out.print("Enter 10 integer values separated by spaces: ");
		for(int i =0; i<10; i++){
			intArray[i] = input.nextInt();
		}
		System.arraycopy(intArray, 0, intArrayCopy, 0, intArray.length);
		Arrays.sort(intArrayCopy);
	}

	public void printArray(){
		System.out.print("The original integer array is: ");
		for(int intValue : intArray)
			System.out.printf("%d ",intValue);
		System.out.print("\nThe sorted integer array is: ");
		for(int intValue: intArrayCopy)
			System.out.printf("%d ",intValue);
		System.out.print("\n");
	}

	public int searchForInt(int v){
		return Arrays.binarySearch(intArrayCopy, v);
	}

	public void printEquality(){
		boolean b = Arrays.equals(intArray, intArrayCopy);
		System.out.printf("intArray %s intArrayCopy\n", (b?"==":"!="));
	}

	public static void main(String args[]){
		UsingArrays useArray = new UsingArrays();
		useArray.printArray();
		useArray.printEquality();
		Scanner input = new Scanner(System.in);
		System.out.print("Which number do you want to find? ");
		int value = input.nextInt();
		int location = useArray.searchForInt(value);
		if(location>=0)
			System.out.printf("Found %d at #%d in the SORTED Array\n",value,location+1);
		else
			System.out.printf("%d is not found\n",value);
	}
}

