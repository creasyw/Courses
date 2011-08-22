import java.util.Scanner;
import java.util.List;
import java.util.LinkedList;
import java.util.ListIterator;

public class ListTest{
	private static final String color[]={"black", "yellow",
		"green","blue","violet","silver","purple"};
	private static final String color2[]={"glod","white",
		"brown","blue","gray","silver"};

	public ListTest(){
		List<String> list1 = new LinkedList<String>();
		List<String> list2 = new LinkedList<String>();

		for(String value : color)
			list1.add(value);
		for(String value : color2)
			list2.add(value);
		list1.addAll(list2);
		list2 = null;
		printList(list1);

		convertToUppercaseString(list1);
		printList(list1);

		int id;
		Scanner input  = new Scanner(System.in);
		while(true){
			System.out.print("\nPlease indicate the index of the color you want to delete: ");
			id = input.nextInt();
			if(id<0 || id>=list1.size()){
				System.out.println("Input invalid. Removing ends.");
				break;
			}
			removeItem(list1, id);
			printList(list1);
			printReversedList(list1);
		}
	}

	public void printList(List<String> list){
		System.out.println("\nlist:");
		for(String color:list)
			System.out.printf("%s ",color);
		System.out.println();
	}

	public void convertToUppercaseString(List<String> list){
		ListIterator<String> iterator = list.listIterator();
		while(iterator.hasNext()){
			String color = iterator.next();
			iterator.set(color.toUpperCase());
		}
	}

	private void removeItem(List<String> list, int index){
		String removed = list.remove(index);
		System.out.printf("The removed item is %s.\n",removed);
	}

	private void printReversedList(List<String> list){
		// add index to set the iterator.
		// This might be another way to achieve RANDOM ACCESS
		ListIterator<String> iterator = list.listIterator(list.size());
		System.out.println("\nReversed list:");
		// using .hasPrevious and .previous are exactly as using .hasNext and .next 
		while(iterator.hasPrevious())
			System.out.printf("%s ",iterator.previous());
	}

	public static void main(String args[]){
		new ListTest();
	}
}


