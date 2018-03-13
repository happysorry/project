package javacsv;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
public class csv{
	public static void main(String[] args){
		String csvfile="C:/Users/User/Desktop/log/半導體.csv";
		String line="";
		String csvSpliter=",";
		String equal="=";
		String id = null,deal = null,ja,f,ticket,million,yester = null,open = null,highest = null,lowest,percent = null,per = null,pbr = null;
		//代號 成交 漲跌價 漲跌幅 成交張數 成交額(百萬) 昨收	開盤	最高	最低	振幅(%)	PER	PBR
		try(BufferedReader br=new BufferedReader(new FileReader(csvfile))){
			while((line=br.readLine())!=null){
				
				String[]country=line.split(",|=");
				for(int i=0;i<16;i++){
					switch(i){
					case 1:
						id=country[i];
					case 5:
						deal=country[i];
						
					case 6:
						ja=country[i];
						
					case 7:
						f=country[i];
						
					case 8:
						ticket=country[i];
					case 9:
						million=country[i];
					case 10:
						yester=country[i];
					case 11:
						open=country[i];
					case 12:
						highest=country[i];
					case 13:
						lowest=country[i];
					case 14:
						percent=country[i];
					case 15:
						per=country[i];
					case 16:
						pbr=country[i];
					default:
						continue;	
					}
					
				}
				if(id.equals('"2330"'))
				System.out.println(id);
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