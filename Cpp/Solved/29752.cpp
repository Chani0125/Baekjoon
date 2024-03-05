#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n, s, ans = 0, now = 0;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> s;
        if (s)
            now++;
        else
        {
            ans = max(ans, now);
            now = 0;
        }
    }

    ans = max(ans, now);
    
    cout << ans << "\n";

    return 0;
}
