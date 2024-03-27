#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n; cin >> n;
    vector<int> v(n+1);
    for (int i = 0; i < n; i++) cin >> v[i+1];

    vector<vector<int>> dp(3, vector<int>(n+1, 0));
    dp[0][v[1]+1] = 1;

    for (int p = v[0]+1; p < n; p++)
    {
        if (dp[0][p] == 0) continue;
        if (p + v[p] > n) continue;
        dp[0][p + v[p]] = dp[0][p] + 1;
    }

    for (int q = n-1; q > 0; q--)
    {
        if (q - v[q] < 0) continue;
        if (dp[0][q] == 0) continue;
        dp[1][q - v[q]] = dp[0][q] + 1;
    }

    for (int q = n-1; q > 0; q--)
    {
        if (q - v[q] < 0) continue;
        if (dp[1][q] == 0) continue;
        dp[1][q - v[q]] = max(dp[1][q - v[q]], dp[1][q] + 1);
    }

    for (int r = 1; r < n; r++)
    {
        if (dp[1][r] == 0) continue;
        if (r + v[r] > n) continue;
        dp[2][r + v[r]] = dp[1][r] + 1;
    }

    for (int r = 1; r < n; r++)
    {
        if (dp[2][r] == 0) continue;
        if (r + v[r] > n) continue;
        dp[2][r + v[r]] = max(dp[2][r + v[r]], dp[2][r] + 1);
    }
    
    for (auto i : dp)
    {
        for (auto j : i)
        {
            cout << j << " ";
        }
        cout << "\n";
    }

    int ans = max(dp[0][n], dp[2][n]);
    if (!ans) ans = -1;
    cout << ans << "\n";
    
    return 0;
}
