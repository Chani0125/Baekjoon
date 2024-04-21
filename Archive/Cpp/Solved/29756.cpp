#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n, k;
    cin >> n >> k;
    vector<int> s(n+1), h(n+1);
    for (int i = 1; i <= n; i++) cin >> s[i];
    for (int i = 1; i <= n; i++) cin >> h[i];

    vector<vector<int>> dp(n+1, vector<int>(101, 0));

    for (int i = 1; i <= n; i++)
    {
        for (int j = 0; j <= 100; j++)
        {
            dp[i][min(100, j+k)] = max(dp[i][min(100, j+k)], dp[i-1][j]);
            if (0 <= min(100, j+k)-h[i])
                dp[i][min(100, j+k)-h[i]] = max(dp[i][min(100, j+k)-h[i]], dp[i-1][j] + s[i]);
        }
    }

    cout << *max_element(dp[n].begin(), dp[n].end()) << "\n";

    return 0;
}
