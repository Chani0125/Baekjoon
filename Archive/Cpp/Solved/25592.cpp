#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n, m = 0;
    cin >> n;

    int t = 0;
    while (t <= n)
    {
        t += ++m;
    }

    int ans = t - n;
    if (m % 2 == 0) ans = 0;
    else if (ans == 0) ans = m;
    cout << ans << "\n";
    
    return 0;
}