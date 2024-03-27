#include <bits/stdc++.h>

#define X first
#define Y second

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n; cin >> n;

    vector<pair<int, int>> t(n, pair<int, int>(0, 0));
    for (int i = 0; i < n; i++)
        cin >> t[i].X >> t[i].Y;
    
    sort(t.begin(), t.end(), [](pair<int, int> X, pair<int, int> Y)
    {
        if (X.X == Y.X) return X.Y < Y.Y;
        else            return X.X < Y.X;
    });
    
    int ans = 0, tmp, next;

    for (int i = 0; i < n; i++)
    {
        next = t[i].Y;
        tmp = 1;
        for (int j = i+1; j < n; j++)
        {
            if (t[j].X >= next)
            {
                next = t[j].Y;
                tmp++;
            }
        }
        ans = max(ans, tmp);
    }

    cout << ans << "\n";

    return 0;
}
