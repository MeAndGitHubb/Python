
#include <iostream>
#include <string.h>
#define _CRT_SECURE_NO_WARNINGS
using namespace std;

#define MAX 100
#define VOCUC 1000 //định nghĩa giá trị MAX

#define inputfile "D:/NGOVOTUANAN_2119110205/LYTHUYETDOTHI/file_test/test2.txt" //định nghĩa đường dẫn tuyệt đối của đồ thị

typedef struct GRAPH{
	int n;//số đỉnh của đồ thị
	int a[MAX][MAX];//ma trận kề của đồ thị
}DOTHI;
//doc ma tran ke
//----------------------
int DocMaTranKe(char sTenFile[100], DOTHI &g);
void XuatMaTranKe(DOTHI g);
int KiemTraMaTranKeHopLe(DOTHI g);
int KiemTraDoThiVoHuong(DOTHI g);

