#include <bits/stdc++.h>

#define X first
#define Y second

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int x, a, b, c, d;
    cin >> x >> a >> b >> c >> d;

    int cent = 0, nickel = 0, dime = 0, quarter = 0;
    int ans[2] = {0, 0};

    nickel += x / 5; cent += x %= 5;

    int tmp = (a - cent) / 5;
    nickel -= tmp;
    cent += tmp * 5;

    cout << cent << nickel << dime << quarter << "\n";
    
    return 0;
}
