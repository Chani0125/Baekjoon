#include <bits/stdc++.h>

using namespace std;

long long dist(vector<pair<int, int>> &x, int y)
{
    long long dist = 0;
    for (int i = 0; i < x.size(); i++)
    {
        if (i == y) continue;
        dist += x[i].second * (i < y ? -1 : 1);
    }
    return abs(dist);
}

int ternary_search(vector<pair<int, int>> &x, int s, int e)
{
    int p, q;
    long long dist_p, dist_q;

    while (e - s >= 3)
    {
        p = (s * 2 + e) / 3;
        q = (s + e * 2) / 3;

        dist_p = dist(x, p);
        dist_q = dist(x, q);

        if (dist_p <= dist_q) e = q;
        else s = p;
    }

    long long dist_new, dist_min = dist(x, s);
    for (int i = s+1; i <= e; i++)
    {
        dist_new = dist(x, i);
        if (dist_new < dist_min)
        {
            dist_min = dist_new;
            s = i;
        }
    }

    return s;
}

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n; cin >> n;

    int y = 0, dy, a = 0;
    vector<pair<int, int>> x(n);
    for (int i = 0; i < n; i++)
    {
        cin >> x[i].first >> x[i].second;
        a += x[i].second;
    }
    sort(x.begin(), x.end());

    int ans = ternary_search(x, 0, n-1);
    cout << x[ans].first << "\n";

    return 0;
}
