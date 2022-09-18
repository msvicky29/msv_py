/*
Programmed by:
MS Vigneswaraa
S Yuvaraj
M Sundaralingam
A.Mohamed Irsath
D.Yugesh
Sanath Jaya suriya
 */

import java.util.*;
class choice
{
	void glyce_check()
	{
		Scanner ob1 = new Scanner(System.in);
		System.out.println("Enter the glycemic index=");
		int glyce;
		
		glyce=ob1.nextInt();
		if(glyce<55)
		{
			System.out.println("Good to eat");
		}
		else if(glyce<70 && glyce>55)
		{
			System.out.println("Try to avoid this food");
		}
		else
		{
			System.out.println("Bad food to eat");
		}
	}
	void good_food()
	{
		System.out.println("NAME\tGlycemic Index Value");
		System.out.println("====   ===================");
		System.out.println("Milk\tless than 55");
		System.out.println("Carrot\tless than55");
		System.out.println("Apple\tless than 55");
		System.out.println("Peanut\t14");
		System.out.println("Bean Sprout\t25");
		System.out.println("Grape\t25");
		System.out.println("Low fat Yogurt\t33");
		System.out.println("Spagheeti\t42");
		System.out.println("Banana\t52");
		System.out.println("Oat meal\t53");
		
		
	}
	void bad_food()
	{
		System.out.println("NAME\tGlycemic Index Value");
		System.out.println("====   ====================");
		System.out.println("Brown Rice\t72");
		System.out.println("Jasmine rice\t89");
		System.out.println("Popcorn\t72");
		System.out.println("White Bread\t70");
		System.out.println("Watermelon\t74");
		System.out.println("Baked potatos\t85");
		System.out.println("Macaroni\t64");
		System.out.println("Honey\t55");
		System.out.println("Ice cream\t61");
		System.out.println("Glucose\t100");
	}
	void type()
	{
		int age;
		System.out.println("Enter your Age=");
		Scanner ob3 = new Scanner(System.in);
		age=ob3.nextInt();
		System.out.println("Your Age is"+age);
		if(age<=6)
		{
			System.out.println("Normal Blood Sugar value is >80 to 180mg/dL");
			System.out.println("Sugar level Before meal is 100 to 180mg/dL");
			System.out.println("Normal  Sugar after 1 or 2 Hrs after eating is 180mg/dL");
		}
		else if(age>6 && age<=20)
		{
			System.out.println("Normal Blood Sugar value is >80 to 180mg/dL");
			System.out.println("Sugar level Before meal is 90 to 180mg/dL");
			System.out.println("Normal  Sugar after 1 or 2 Hrs after eating is,Upto 140mg/dL");
		}
		else if(age>20 && age<=35)
		{
			System.out.println("Normal Blood Sugar value is >70 to 150mg/dL");
			System.out.println("Sugar level Before meal is 90 to 180mg/dL");
			System.out.println("Normal  Sugar after 1 or 2 Hrs after eating is ,Upto 140mg/dL");
		}
		else
		{
			System.out.println("Normal Blood Sugar value is >60 to 140mg/dL");
			System.out.println("Sugar level Before meal is 80 to 160mg/dL");
			System.out.println("Normal  Sugar after 1 or 2 Hrs after eating is ,Upto 130mg/dL");
		}
		
	}
}
public class aa
{
	public static void main(String[] args)
	{   
		 int ch;
		 System.out.println("=========Health Care Center=============");
		   System.out.println("1)Type 1 or Type 2                     |");
		   System.out.println("2)Best food for Diabetes Patients      |");
		   System.out.println("3)Worst food for Diabetes Patients     |");
		   System.out.println("4)Check Glycemic Index                 |");
		   
		   System.out.println("5)Exit                                 |");
		   System.out.println("========================================");
		 do {
		  
		  
		   Scanner ob2 =new Scanner(System.in);
		   System.out.println("Enter your Choice:");
		   ch=ob2.nextInt();
		   choice result = new choice();
		   switch(ch)
		   {
		   case 1:
		   {
			   result.type(); 
			   System.out.println("");
			   System.out.println("");
			   break;
		   }
		   case 2:
		   {
			   result.good_food();
			   System.out.println("");
			   System.out.println("");
			   break;
		   }
		   case 3:
		   {
			   result.bad_food();
			   System.out.println("");
			   System.out.println("");
			   break;
		   }
		   case 4:
		   {
			   result.glyce_check();
			   System.out.println("");
			   System.out.println("");
			   break;
		   }
		   case 5:
		   {
			   System.out.println("Program Ended.......");
			   System.out.println("");
			   break;
		   }
		  default:
		  {
			   System.out.println("Please,Enter valid Choice Only.....");  
			   break;
			   
		   }
		 }
	   }while(ch!=5);
	}
}