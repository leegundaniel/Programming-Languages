#include <iostream>
#include <cmath>
using namespace std;
int sub1( ) {
	int x = 10;
	double sum = 0;
	for(int k=0; k<10; k++) {
		cout << "x = " << x << endl;
		double x = pow(2.0,k);
		sum += x;
	}
	 cout << "sum = " << sum << endl;
   return sum;
}



int main() {
 
  sub1();
}