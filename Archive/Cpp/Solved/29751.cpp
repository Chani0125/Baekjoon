#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int w, h;
    cin >> w >> h;

    cout << fixed;
    cout.precision(1);
    cout << (double)w * h / 2 << "\n";
    
    return 0;
}
