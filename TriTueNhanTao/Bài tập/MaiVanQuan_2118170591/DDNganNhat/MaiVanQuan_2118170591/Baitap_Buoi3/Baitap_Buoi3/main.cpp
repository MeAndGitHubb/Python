#include <iostream>
using namespace std;

int main() {
	int cho, ga;
	int sum, changa,chancho,tong;

	cout << "\nNhap so chan ga" << endl;
	cin >> changa;
	cout << "\nNhap so chan cho" << endl;
	cin >> chancho;
	cho = (chancho * 4);
	ga = (changa *2);
	tong = (cho + ga);

	cout << "So ga= " << ga;

	cout << "\nSo cho= " << cho;
	cout << "\nTong so chan= " << tong;
}