#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n; cin >> n;
    vector<vector<int>> v(n);

    int x;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            cin >> x;
            v[i].push_back(x);
        }
    }

    for (int i = n-1; i > 0; i--)
    {
        for (int j = 0; j < i; j++)
        {
            v[i-1][j] += max(v[i][j], v[i][j+1]);
        }
    }

    cout << v[0][0] << "\n";
    
    return 0;
}
