package activities;


import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;


public class CRM_Activity2 {
	WebDriver driver;
	
	@BeforeMethod
	public void open_Browser() {
	driver= new FirefoxDriver();
	driver.get("http://alchemy.hguy.co/crm");
	}
	
	@AfterMethod
	public void close_browser() {
		driver.close();
	}
	
	@Test
	public void get_url() {
		WebElement title= driver.findElement(By.xpath("//*[@class='companylogo']/img"));
		System.out.println(title.getAttribute("src"));
		
	}
	

}