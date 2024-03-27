#include <bits/stdc++.h>

using namespace std;

int arr[] = {1, 2, 5, 26, 677};

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int t, n, l;
    cin >> t;

    while (t--)
    {
        vector<vector<int>> dp(l, vector<int>(n, 0));
        dp[0][n-1] = 1;

        int last_num = n;
        for (int i = 1; i < l; i++)
        {
            for (int j = 0; j < last_num; j++)
            {
                if (dp[i-1][j])
                {
                    int a = sqrt(j+1);
                    if (a * a == j+1) a--;
                    for (int k = 0; k < a; k++)
                        dp[i][k]++;
                    last_num = max(last_num, a);
                }
            }
        }

        for (auto i : dp) {for (auto j : i) cout << j << " "; cout << "\n";}

        int sum = 0;
        for (auto i : dp[l-1]) sum += i;
        cout << sum << "\n";
    }
    
    return 0;
}
