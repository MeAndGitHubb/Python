#include "dothi.h"
int DocMaTranKe(char sTenFile[100], DOTHI &g)
{
	FILE*f;//một biết FILE
	fopen_s(&f, sTenFile, "r");// mở một gile có đường dẫn là TenFile
	if (f == NULL)// nếu file mở được thì biến f!=NULL và file không biến f==NULL
	{
		cout << "khong mo duoc file\n";
		return 0;
	}
	fscanf_s(f, "%d", &g.n);
	for (int i = 0; i < g.n; i++)
	{
		for (int j = 0; j < g.n; j++)
			fscanf_s(f, "%d", &g.a[i][j]); //đọc từng dòng va gán giá trị
	}
	fclose(f);//đóng file đã mở
	return 1;
}
//---------------------------
void XuatMaTranKe(DOTHI g)
{
	cout << "So dinh cua do thi la" << g.n<<"\n";
	cout << "Ma tran ke cua do thi la\n";
	for (int i = 0; i < g.n; i++)
	{
		cout << "\t";
		for (int j = 0; j < g.n; j++)
		{
			cout << g.a[i][j];
		}
		cout << "\n";
	}
}
// Kiem tra ma tran ke
int KiemTraMaTranKeHopLe(DOTHI g)
{
	for (int i=0; i < g.n; i++)
	{
		if (g.a[i][i] != 0)
			return 0;
	}
	return 1;
}
//-----------------
int KiemTraDoThiVoHuong(DOTHI g)
{
	for (int i = 0; i < g.n; i++)
	{
		for (int j = 0; j < g.n; j++)
		{
			if (g.a[i][j] != g.a[j][i])
				return 0;
		}
		return 1;
	}
}