#include <bits/stdc++.h>

#define X first
#define Y second

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n; cin >> n;

    vector<int> s(n, 0);
    vector<vector<int>> t(n, vector<int>(n));

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> t[i][j];
    
    int max_idx = 0;
    for (int i = 0; i < n; i++)
    {
        max_idx = 0;
        for (int j = 1; j < n; j++)
            if (t[n-1-s[j]][j] > t[n-1-s[max_idx]][max_idx])
                max_idx = j;
        s[max_idx]++;
    }

    s[max_idx]--;
    cout << t[n-1-s[max_idx]][max_idx];
    
    return 0;
}
