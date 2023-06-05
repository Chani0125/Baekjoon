#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, k;
    cin >> n >> k;

    vector<pair<int, int>> v(n);
    for (int i = 0; i < n; i++)
        cin >> v[i].first >> v[i].second;
    
    vector<int> b(k+1, 0);
    for (int i = 0; i < n; i++)
        for (int j = k-v[i].first; j >= 0; j--)
            b[j+v[i].first] = max(b[j+v[i].first], b[j] + v[i].second);
    
    int ans = 0;
    for (auto i : b) ans = max(ans, i);
    cout << ans << "\n";

    return 0;
}