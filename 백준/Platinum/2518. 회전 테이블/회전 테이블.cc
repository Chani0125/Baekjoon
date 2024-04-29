#include <bits/stdc++.h>

#define vi vector<int>
#define vvi vector<vector<int>>
#define vvvi vector<vector<vector<int>>>
#define vvvvi vector<vector<vector<vector<int>>>>
#define INF 100000000

using namespace std;

int n, m1, m2, m3;

int dist(int &f, int &t)
{
    if (f == t) return 0;
    int r = f - t; int l = t - f;
    if (r < 0) r += n;
    if (l < 0) l += n;
    return min(r, l);
}

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    cin >> n;

    cin >> m1; vi a(m1+1);
    for (int i = 1; i <= m1; i++)
        cin >> a[i];
    cin >> m2; vi b(m2+1);
    for (int i = 1; i <= m2; i++)
        cin >> b[i];
    cin >> m3; vi c(m3+1);
    for (int i = 1; i <= m3; i++)
        cin >> c[i];
    
    for (auto &i : b)
    {
        i -= n / 3;
        if (i < 1) i += n;
    }
    for (auto &i : c)
    {
        i -= (n / 3) * 2;
        if (i < 1) i += n;
    }

    a[0] = 1; b[0] = 1; c[0] = 1;

    vvvvi dp(m1+1, vvvi(m2+1, vvi(m3+1, vi(3, INF))));

    dp[0][0][0][0] = 0;

    for (int t = 1; t <= m1+m2+m3; t++)
    {
        for (int i = 0; i <= min(t, m1); i++)
        {
            for (int j = 0; j <= min(t-i, m2); j++)
            {
                int k = t-i-j;
                if (k > m3) continue;

                if (i > 0)
                {
                    dp[i][j][k][0] = min(dp[i][j][k][0], dp[i-1][j][k][0] + dist(a[i-1], a[i]));
                    dp[i][j][k][0] = min(dp[i][j][k][0], dp[i-1][j][k][1] + dist(b[j],   a[i]));
                    dp[i][j][k][0] = min(dp[i][j][k][0], dp[i-1][j][k][2] + dist(c[k],   a[i]));
                }
                if (j > 0)
                {
                    dp[i][j][k][1] = min(dp[i][j][k][1], dp[i][j-1][k][0] + dist(a[i],   b[j]));
                    dp[i][j][k][1] = min(dp[i][j][k][1], dp[i][j-1][k][1] + dist(b[j-1], b[j]));
                    dp[i][j][k][1] = min(dp[i][j][k][1], dp[i][j-1][k][2] + dist(c[k],   b[j]));
                }
                if (k > 0)
                {
                    dp[i][j][k][2] = min(dp[i][j][k][2], dp[i][j][k-1][0] + dist(a[i],   c[k]));
                    dp[i][j][k][2] = min(dp[i][j][k][2], dp[i][j][k-1][1] + dist(b[j],   c[k]));
                    dp[i][j][k][2] = min(dp[i][j][k][2], dp[i][j][k-1][2] + dist(c[k-1], c[k]));
                }
            }
        }
    }

    cout << *min_element(dp[m1][m2][m3].begin(), dp[m1][m2][m3].end()) << "\n";

    return 0;
}
