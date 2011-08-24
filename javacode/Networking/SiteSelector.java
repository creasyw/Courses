import java.net.MalformedURLException;
import java.net.URL;
import java.util.HashMap;
import java.util.ArrayList;
import java.awt.BorderLayout;
import java.applet.AppletContext;
import javax.swing.JApplet;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JScrollPane;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;

public class SiteSelector extends JApplet
{
	private HashMap<Object, URL> sites;
	private ArrayList<String> siteNames;
	private JList siteChooser;

	public void init()
	{
		sites = new HashMap<Object,URL>();
		siteNames = new ArrayList<String>();

		getSitesFromHTMLParameters();

		add(new JLabel("Choose a site to browse"),BorderLayout.NORTH);

		siteChooser = new JList(siteNames.toArray());
		siteChooser.addListSelectionListener(new ListSelectionListener()
		{
			public void valueChanged(ListSelectionEvent event)
			{
				Object object = siteChooser.getSelectedValue();
				URL newDocument = sites.get(object);
				AppletContext browser = getAppletContext();
				browser.showDocument(newDocument);
			}
		}
		);

		add(new JScrollPane(siteChooser),BorderLayout.CENTER);
	}

	private void getSitesFromHTMLParameters()
	{
		String title;
		String location;
		URL url;
		int counter = 0;

		title = getParameter("title"+counter);

		while(title!=null)
		{
			location = getParameter("location"+counter);
			try
			{
				url = new URL(location);
				sites.put(title,url);
				siteNames.add(title);
			}
			catch(MalformedURLException urlException)
			{
				urlException.printStackTrace();
			}
			++counter;
			title = getParameter("title"+counter);
		}
	}
}




