#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n, m, q;
    cin >> n >> m >> q;
    vector<vector<int>> a(n+1, vector<int>(m+1));
    vector<int> w(q);
    vector<int> p(q);

    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++)
            cin >> a[i][j];

    for (int i = 0; i < q; i++)
        cin >> w[i] >> p[i];
    
    vector<vector<int>> b(n+1, vector<int>(m+1));
    b[1] = a[1];
    for (int i = 2; i <= n; i++)
        for (int j = 1; j <= m; j++)
            b[i][j] = a[i][j] + b[i-1][j-1] + b[i-1][j] - b[i-2][j-1];
    
    // for (auto i : b) {for (auto j : i) cout << j << " "; cout << "\n";}

    for (int i = 0; i < q; i++)
        cout << b[w[i]][p[i]] << "\n";            
    
    return 0;
}
