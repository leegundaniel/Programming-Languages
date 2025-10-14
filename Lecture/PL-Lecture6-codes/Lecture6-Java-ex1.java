class Main {
final String s = "global";
	String sub1( ) { return s; }
	String sub2(int which) {
		String s = "local"; 
		if ( which == 1 ) return sub1();
		else return s;
	}
	void  ScopeHole( ) {
		System.out.println("0: s = " + s );
		System.out.println("1: s = " + sub2(1) );
		System.out.println("2: s = " + sub2(2) );
  }


  public static void main(String[] args) {
   Main object = new Main();
   object.ScopeHole();
  }
}