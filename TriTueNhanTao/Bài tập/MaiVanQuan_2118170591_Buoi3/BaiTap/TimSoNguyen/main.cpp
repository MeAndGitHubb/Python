#include <iostream>


int x[10], n, k, count;

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
void init()
{
	printf("k = "); scanf("%d", &k);
	printf("n = "); scanf("%d", &n);
	count = 0;
}





void main()
{
	Try(1);
	PrintResult();
}