import java.util.*;
abstract class Shape
{
	abstract double area();
}
class Rectangle extends Shape
{	
	double l,w;
	Rectangle(double length, double width)
	{	
		l=length;
		w=width;
	}
	double area()
	{
		return l*w;
	}
}
class Triangle extends Shape
{	
	double l,w;
	Triangle(double length, double width)
	{	
		l=length;
		w=width;
	}
	double area()
	{
		return l*w*0.5;
	}
}
class Abs
{
	public static void main(String args[])
	{
		Rectangle r=new Rectangle(10,20);
		Triangle t=new Triangle(3,2);
		System.out.println("Rectangle: "+r.area());
		System.out.println("Triangle: "+t.area());
	}
}


		