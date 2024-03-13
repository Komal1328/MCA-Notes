class cal
{
	public static void main(String args[])
	{
		int x,y,i;
		char op;
		try
		{
			if(args.length==3)
			{
				x=Integer.parseInt(args[0]);
				y=Integer.parseInt(args[2]);
				op=args[1].charAt(0);
				System.out.println("First number: "+x);
				System.out.println("second number: "+y);
				if(op=='+')
					System.out.println("Sum of "+x+" and "+y+" is: "+(x+y));
				else if(op=='-')
					System.out.println("Subtraction of "+x+" and "+y+" is: "+(x-y));
				else if(op=='*')
					System.out.println("Multiplication of "+x+" and "+y+" is: "+(x*y));	
				else if(op=='/')
					System.out.println("Division of "+x+" and "+y+" is: "+(x/y));
				else
					System.out.println("Invalid input");
			}
			else
				System.out.println("Invalid Input");
		}
		catch (NumberFormatException e)
		{	
			System.out.println("Invalid input");
		}
	
	}
}		