package yahoostock;
import java.net.*;
import java.net.URLConnection;
import java.nio.ByteBuffer;
import java.util.List;
import java.util.ArrayList;
import java.io.*;


public class stock {

	static ArrayList<String>col01=new ArrayList<String>();
	static ArrayList<String>col03=new ArrayList<String>();
	static String urldata=null;
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String url="https://tw.stock.yahoo.com/s/list.php?c=%A4%F4%AAd&rr=0.45967800%201521364543";
		try{
			URL url1=new URL(url);
			//URL定址連線
			//System.out.println("22");
			URLConnection conn=url1.openConnection();
			InputStream in=conn.getInputStream();//取得串流
			BufferedInputStream bis=new BufferedInputStream(in);
			ByteArrayOutputStream baf=new ByteArrayOutputStream();
			//System.out.println("av"+bis.available());
			int da=0;
			System.out.println("before");
			//System.out.println(bis.available());
			byte[] data = new byte[5000];//store in baf
			while((da = bis.read(data)) != -1){  
		           baf.write(data,0,da);  
		     }
			System.out.println("After");
			//System.out.println(baf);
			urldata=new String(baf.toByteArray(),"BIG5");
			//System.out.println(urldata);
		}catch(IOException e){
			e.printStackTrace();
		}
		//
		Parser(urldata);
		System.out.println(col01.get(1).toString());
		/*for(int i=0;i<col01.size();i++)
			System.out.println(col01.get(i).toString());*/
	}
	
	public static void Parser(String urldata){
		String temp=null;
		int start=0,end=0,counter=0;
		do{
			start=urldata.indexOf("<td align=center bgcolor=#FFFfff nowrap><a href=",end+1);
			end=urldata.indexOf("</a><br>",start+1);
			System.out.println(start);
			System.out.println(end);
			temp=urldata.substring(start+63, end);
			col01.add(temp);
			
			start=urldata.indexOf("<td align=\"center\" bgcolor=\"#FFFfff\" nowrap><b>",end+1);
			end=urldata.indexOf("</b></td>",start+1);
			//System.out.println(start);
			//System.out.println(end);
			temp=urldata.substring(start+47, end);
			col03.add(temp);
			counter++;
			//System.out.println(start);
		}while(counter<7);
	}

}
