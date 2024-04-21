#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n;
    cin >> n;
    vector<vector<int>> v(n+1, vector<int>(3, 0));

    int r, g, b;
    for (int i = 1; i <= n; i++)
    {
        cin >> r >> g >> b;
        v[i][0] = min(v[i-1][1] + r, v[i-1][2] + r);
        v[i][1] = min(v[i-1][0] + g, v[i-1][2] + g);
        v[i][2] = min(v[i-1][0] + b, v[i-1][1] + b);
    }
    
    cout << *min_element(v[n].begin(), v[n].end()) << "\n";
    
    return 0;
}
