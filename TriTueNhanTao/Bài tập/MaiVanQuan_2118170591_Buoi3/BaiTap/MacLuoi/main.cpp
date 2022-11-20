#include <iostream>


int a[10], x[10], n, k, count;
int i;

void PrintResult(){
	count++;
	printf("%5d", count);
	for (i = 1; i <= n; i++)
		if (x[i] == 1)
			printf("%3d", a[i]);
	printf("\n");
}
void Try(int i)
{
	int j;
	for (j = 0; j <= 1; j++)
	{
		x[i] = j;
		if (i == n) PrintResult;
		else Try(i + 1);

	}
}

void init() {
	printf("n=");
	scanf_s("%d", &n);
	for (i = 1; i <= n; i++)
	{
		printf("\n a[%d]=", i);
		scanf_s("%d", &a[i]);
	}
	count = 0;
}


		
void main()
		{
			init();
			Try(1);
			PrintResult();
		}