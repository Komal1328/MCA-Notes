import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
class Employee
{
	String emp_id,emp_name,desg,b;
	int basic,tot;
	InputStreamReader reader= new InputStreamReader(System.in);
	BufferedReader br=new BufferedReader(reader);
	void set_emp() 
	{
		try
		{
			System.out.print("Enter employee name: ");
			emp_name=br.readLine();
			System.out.print("Enter employee Id: ");
			emp_id=br.readLine();
			System.out.print("Enter employee Designation: ");
			desg=br.readLine();
			System.out.print("Enter employee basic salary: ");
			b=br.readLine();
			basic=Integer.parseInt(b);
		}
		catch (Exception e)
		{
			System.out.println(e);
		}
	}
	void display()
	{
		System.out.println("Employee Details:");
		System.out.println("Name: "+emp_name);
		System.out.println("ID: "+emp_id);
		System.out.println("Designation: "+desg);
		tot=(80*basic)/100+(20*basic)/100+basic;
		System.out.println("Total: "+tot);
	}
}
class emp
{
	public static void main(String args[]) throws IOException
	{
		Employee e=new Employee();
		e.set_emp();
		e.display();
	}
}
		