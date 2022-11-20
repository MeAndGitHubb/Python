#include <iostream>
#include <conio.h>
using namespace std;

int ucln(int, int);

int x, y;
int vx, vy;
int z;

int luat1();
int luat2();
int luat3();

int main()
{
    cout << "Bai Toan Dong Nuoc" << endl;
    cout << "Nhap dung tich binh X: ";
    cin >> vx;
    cout << "Nhap dung tich binh Y: ";
    cin >> vy;
    cout << "Nhap dung tich can dong: z = ";
    cin >> z;

    if (z % ucln(vx, vy) != 0)
    {
        cout << "Khong the dong duoc theo yeu cau!" << endl;
    }
    else
    {
        x = 0;
        y = 0;
        while (x != z && y != z)
        {
            luat1();
            luat2();
            luat3();
        }
    }
    _getch();
    return 0;
}

int ucln(int a, int b)
{
    if (a <= 0 || b <= 0)
        return 1;
    while (a % b != 0 && b % a != 0)
    {
        if (a > b)
            a = a % b;
        else
            b = b % a;
    }
    return a > b ? b : a;
}
int luat1()
{
    if (x == vx)
    {
        x = 0;
        cout << "Luat L1 -> x = " << x << ", y = " << y << endl;
        return 1;
    }
    return 0;
}
int luat2()
{
    if (y == 0)
    {
        y = vy;
        cout << "Luat L2 -> x = " << x << ", y = " << y << endl;
        return 1;
    }
    return 0;
}
int luat3()
{
    if (x < vx && y > 0)
    {
        if (y > vx - x)
        {
            y -= vx - x;
            x = vx;
        }
        else
        {
            x += y;
            y = 0;
        }
        cout << "Luat L3 -> x = " << x << ", y = " << y << endl;
        return 1;
    }
    return 0;
}