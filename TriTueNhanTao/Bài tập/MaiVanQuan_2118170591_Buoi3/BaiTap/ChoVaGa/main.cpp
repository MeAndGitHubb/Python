#include <iostream>
using namespace std;

int main() {
	int dog, chicken;
	int sum, sumFeet;

	cout << "Please input the number of dog and chicken" << endl;
	cin >> sum;
	cout << "\nPlease input the sum of feet" << endl;
	cin >> sumFeet;
	dog = (sumFeet - 2 * sum) / 2;
	chicken = sum - dog;
	if (dog > 0 && chicken > 0) {
		cout << "The number of dog is " << dog << endl;
		cout << "The number of chicken is " << chicken << endl;
	}
	else {
		cout << "invalid" << endl;
	}
}