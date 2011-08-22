import java.util.StringTokenizer;
import java.util.Map;
import java.util.HashMap;
import java.util.Set;
import java.util.TreeSet;
import java.util.Scanner;

public class WordTypeCount
{
	private Map<String,Integer> map;
	private Scanner scanner;

	public WordTypeCount()
	{
		map = new HashMap<String,Integer>();
		scanner = new Scanner(System.in);
		createMap();
		displayMap();
	}

	private void createMap()
	{
		System.out.println("Enter a string:");
		String input = scanner.nextLine();
		StringTokenizer tokenizer = new StringTokenizer(input);
		
		while(tokenizer.hasMoreTokens())
		{
			String word = tokenizer.nextToken().toLowerCase();
			word = removePunctuation(word);
			if(map.containsKey(word))
			{
				int count = map.get(word);
				map.put(word, count+1);
			}
			else
				map.put(word,1);
		}
	}

	private String removePunctuation(String string)
	{
		return string.replaceAll("\\W","");
	}

	private void displayMap()
	{
		Set<String> keys = map.keySet();
		TreeSet<String> sortedKeys = new TreeSet<String>(keys);
		System.out.println("Map contains:\nKey\t\tValue");

		for(String key : sortedKeys)
			System.out.printf("%-10s%10s\n",key,map.get(key));
		System.out.printf("\nsize: %d\nisEmpty: %b\n",map.size(),map.isEmpty());
	}

	public static void main(String args[])
	{
		new WordTypeCount();
	}
}
