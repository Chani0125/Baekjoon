#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    vector<int> v, c, k;
    vector<int> dp(m+1, 0);

    for (int i = 0; i < n; i++)
    {
        int v, c, k;
        cin >> v >> c >> k;
        for (int r = 1; k > 0; r <<= 1)
        {
            int w = min(r, k);
            for (int j = m; j >= v*w; j--)
            {
                dp[j] = max(dp[j], dp[j - v*w]+c*w);
            }
            k -= w;
        }
    }

    cout << dp[m];

    return 0;
}
