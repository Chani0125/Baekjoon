#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n, m;
    cin >> n >> m;

    int tmp;
    vector<vector<int>> v(n+1, vector<int>(n+1, 0));
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            cin >> tmp;
            v[i][j] = tmp + v[i-1][j] + v[i][j-1] - v[i-1][j-1];
        }
    }
    
    int x1, x2, y1, y2;
    for (int i = 0; i < m; i++)
    {
        cin >> x1 >> y1 >> x2 >> y2;
        cout << v[x2][y2] - v[x1-1][y2] - v[x2][y1-1] + v[x1-1][y1-1] << "\n";
    }

    return 0;
}
