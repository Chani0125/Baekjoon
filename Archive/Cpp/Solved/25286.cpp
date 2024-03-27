#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    int t; cin >> t;
    while (t--)
    {
        int y, m, d;
        cin >> y >> m;
        if (m == 1)
        {
            y--; m = 12; d = 31;
        }
        else if (m == 3)
        {
            m--;
            if ((y % 400 == 0) || (y % 100 != 0 && y % 4 == 0)) d = 29;
            else d = 28;            
        }
        else if (m == 2 || m == 4 || m == 6 || m == 8 || m == 9 || m == 11)
        {
            m--; d = 31;
        }
        else
        {
            m--; d = 30;
        }
        cout << y << " " << m << " " << d << endl;
    }
    return 0;
}