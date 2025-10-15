class Main {
public Main(String value ){
Name = value;

}
private String Name;

void sub1( ) {
	int x = 10;
	double sum = 0;
	for(int k=0; k<10; k++) {
    
		System.out.println( "x = " + x ) ;
     x =  (int) Math.pow(2.0,(double)k);
		sum += x;
	}
	 System.out.println("sum = " + sum );
}





int sum(int n) {
		 int sum =1; // local name = method name
		for(int k=1; k<=n; k++) {
      
			 sum = sum + k;
		}
		return sum;
	}
  public static void main(String[] args) {
    Main object = new Main(""); 
    //object.sub1();
    System.out.println(object.sum(5));
    System.out.println("Hello world!");
  }
}