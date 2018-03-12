package javacsv;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
public class csv{
	public static void main(String[] args){
		String csvfile="C:/Users/User/Desktop/data/0050.csv";
		String line="";
		String csvSpliter=",";
		
		try(BufferedReader br=new BufferedReader(new FileReader(csvfile))){
			while((line=br.readLine())!=null){
				
				String[]country=line.split(csvSpliter);
				for(int i=0;i<6;i++)
				System.out.println("country="+country[i]);
				
			}
		}
		catch (FileNotFoundException e){
			e.printStackTrace();
		}
		catch (IOException e){
			e.printStackTrace();
		}
		
	}
}