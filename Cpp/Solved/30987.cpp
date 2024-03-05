#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int x1, x2;
    cin >> x1 >> x2;
    int a, b, c, d, e;
    cin >> a >> b >> c >> d >> e;

    a = a / 3;
    b = (b - d) / 2;
    c = c - e;
    
    int ans = (x2*x2*x2-x1*x1*x1)*a + (x2*x2-x1*x1)*b + (x2-x1)*c;
    
    cout << ans << "\n";
    
    return 0;
}
