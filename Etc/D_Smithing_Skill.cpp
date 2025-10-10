#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n, m;
    cin >> n >> m;

    vector<pair<int, int>> v(n);
    for (auto &i : v) cin >> i.first;
    for (auto &i : v) cin >> i.second;
    vector<int> c(m);
    for (auto &i : c) cin >> i;

    sort(v.begin(), v.end(), [](pair<int, int> a, pair<int, int> b) {
        return a.first-a.second < b.first-b.second;
    });

    long long exp = 0;
    for (auto i : v)
    {
        int a = i.first;
        int b = i.second;

        for (auto &j : c)
        {
            if (j >= a)
            {
                int t = (j-a) / (a-b) + 1;
                exp += t * 2;
                j -= t * (a-b);
            }
        }
    }

    cout << exp << "\n";
    
    return 0;
}
