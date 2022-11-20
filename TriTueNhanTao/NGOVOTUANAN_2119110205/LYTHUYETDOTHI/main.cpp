#include "dothi.h"
int main()
{
	DOTHI g;
	system("cls");
	if (DocMaTranKe(inputfile, g) == 1)
	{
		cout << "Da lay thong tin do thi tu file thanh cong\n\n";
		XuatMaTranKe(g);
		cout << "Bam 1 phim bat ki de tien hanh kiem tra do thi...\n\n";
		system("pause");
		if (KiemTraMaTranKeHopLe(g) == 1)
			cout << "Do thi hop le.\n";
		else
			cout << "Do thi khong hop le\n.";
		if (KiemTraDoThiVoHuong(g) == 1)
			cout << "Do thi vo huong.\n";
		else
			cout << "Do thi co huong,\n";
	}
	system("pause");
	return 0;
}