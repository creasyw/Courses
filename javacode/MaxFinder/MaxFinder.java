import java.util.Scanner;

public class MaxFinder{
	public void determineMaximum(){
		Scanner input = new Scanner(System.in);

		System.out.print("Enter three floating-point values separated by spaces: ");
		double n1 = input.nextDouble();
		double n2 = input.nextDouble();
		double n3 = input.nextDouble();

		double result = maximum(n1, n2, n3);

		System.out.println("Maximum is: "+result);
	}

	public double maximum(double x, double y, double z){
		double value = x;
		if(y>value)
			value = y;
		if(z>value)
			value = z;
		return value;
	}
}

