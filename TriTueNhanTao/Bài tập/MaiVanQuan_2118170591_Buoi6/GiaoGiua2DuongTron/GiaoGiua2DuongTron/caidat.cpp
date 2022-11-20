#include "Khaibao.h"
int Vx, Vy, z;


int C1,C2;
int A1, A2;
int T1, T2;
int a,b;
int R1, R2;
int x;
int s1, s2, s;

void Nhapmang()
{
	printf("\nNhap du lieu\n");
	printf("\nNhap R1: ");
	scanf_s("%d", &R1);
	printf("\nNhap R2: ");
	scanf_s("%d", &R2);
	printf("\nNhap a: ");
	scanf_s("%d", &a);
	printf("\nNhap b: ");
	scanf_s("%d", &b);
	printf("\nNhap s: ");
	scanf_s("%d", &s);
}
void Xuatmang()
{
	printf("\n\nDu lieu vua nhap:");
	printf("R1=%d ", R1);
	printf("R2=%d ", R2);
	printf("a=%d ", a);
	printf("b=%d ", b);
	printf("a=%d ", s);
}
int giaonhau()
{
	int S1,S2,S;
	printf("\n\nBai Lam:");
	C1 = R1;
	C2 = R2;
	A1 = a; 
	A2 = a;
	T1= R1;
	T1 = R1;
	T1 = x;
	T2 = R2;
	T1 = R2;
	T1 = x;
	S1= A1*s - T1*s;
	S2= A2*s - T2*s;
	S = S1 + S2;
	printf("\n\nKetqua:");
	printf("a=%d ", S1);
	printf("\n\nKetqua:");
	printf("a=%d ", S2);
	printf("\n\nKetqua:");
	printf("a=%d ", S);
	return 0;
}