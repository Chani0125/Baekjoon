#include <bits/stdc++.h>

#define vi vector<int>
#define vvi vector<vector<int>>
#define vvvi vector<vector<vector<int>>>
#define vvvvi vector<vector<vector<vector<int>>>>
#define INF INT_MAX

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

    cin >> m1; vi a(m1);
    for (auto &i : a)
        cin >> i;
    cin >> m2; vi b(m2);
    for (auto &i : b)
        cin >> i;
    cin >> m3; vi c(m3);
    for (auto &i : c)
        cin >> i;
    
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

    vvvvi dp(m1+1, vvvi(m2+1, vvi(m3+1, vi(2))));

    dp[0][0][0][1] = 1;

    for (int t = 1; t <= m1+m2+m3; t++)
    {
        for (int i = 0; i <= min(t, m1); i++)
        {
            for (int j = 0; j <= min(t-i, m2); j++)
            {
                int k = t-i-j;
                if (k > m3) continue;

                int min_ = INF;
                int from_ = dp[i][j][k][1];

                if (i > 0 && min_ >= dp[i-1][j][k][0] + dist(dp[i-1][j][k][1], a[i-1]))
                {
                    min_ = dp[i-1][j][k][0] + dist(dp[i-1][j][k][1], a[i-1]);
                    from_ = a[i-1];
                }
                if (j > 0 && min_ >= dp[i][j-1][k][0] + dist(dp[i][j-1][k][1], b[j-1]))
                {
                    min_ = dp[i][j-1][k][0] + dist(dp[i][j-1][k][1], b[j-1]);
                    from_ = b[j-1];
                }
                if (k > 0 && min_ >= dp[i][j][k-1][0] + dist(dp[i][j][k-1][1], c[k-1]))
                {
                    min_ = dp[i][j][k-1][0] + dist(dp[i][j][k-1][1], c[k-1]);
                    from_ = c[k-1];
                }

                dp[i][j][k][0] = min_;
                dp[i][j][k][1] = from_;
                
            }
        }
    }

    cout << dp[m1][m2][m3][0] << "\n";

    return 0;
}
