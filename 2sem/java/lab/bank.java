import java.util.*;
class Bank_account
{
	double bal=0;
	void deposite(double amt)
	{
		bal=bal+amt;
		System.out.println("Balance amount: "+bal);
	}
	void withdraw(double amount)
	{
		bal=bal-amount;
		System.out.println("Balance amount in bank_account: "+bal);
	}
}
class saving extends Bank_account
{
	void withdraw(double amount)
	{
		System.out.println("Balance amount in savings account: "+bal);
		if(bal>100)
		{
			bal=bal-amount;
			System.out.println("Balance amount in savings account: "+bal);	
		}
		else
		{
			System.out.println("Insuffient balance in savings account: "+bal);
		}
	}
}
class current extends Bank_account
{
	void withdraw(double amount)
	{
		bal=bal-amount;
		System.out.println("Balance amount in current account: "+bal);	
	}
}
class bank
{	
	public static void main(String args[])
	{
		saving s=new saving();
		current c=new current();
		s.deposite(5000);
		s.withdraw(4900);
		c.deposite(4000);
		c.withdraw(3500);
		s.withdraw(100);
		c.withdraw(500);
	}
}
	