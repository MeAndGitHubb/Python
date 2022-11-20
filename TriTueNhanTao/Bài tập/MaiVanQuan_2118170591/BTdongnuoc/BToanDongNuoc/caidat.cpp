#include "KhaiBao.h"
int Vx, Vy, z;
void Nhapmang()
{
	printf("\nGoi Vx la binh trai- Goi Vy la binh phai\n");
	printf("\nNhap Vx: ");
	scanf_s("%d", &Vx);
	printf("\nNhap Vy: ");
	scanf_s("%d", &Vy);
	printf("\nNhap z: ");
	scanf_s("%d", &z);
}
void Xuatmang()
{
	printf("\n\nDu lieu vua nhap:");
	printf("Vx=%d ", Vx);
	printf("Vy=%d ", Vy);
	printf("z=%d ", z);
}
int giatrinho(int a, int b)
{
	return a>b ? b : a;
}
int BTdongnuoc()
{
	int x, y, k;
	printf("\n\nBai Lam:");
	x = 0; y = 0;
	while ((x != z) && (y != z))
	{
		if (x == Vx)
		{
			x = 0;
			printf("\nLuat 1: x=%d ", x);
			printf(" y=%d ", y);
		}
		if (y == 0)
		{
			y = Vy;
			printf("\n\nLuat 2: x=%d", x);
			printf(" y=%d", y);
		}
		if (y>0)
		{
			k = giatrinho(Vx - x, y);
			x = x + k;
			y = y - k;
			printf("\nLuat 3: x=%d", x);
			printf(" y=%d", y);
		}
	}
	return 0;
}