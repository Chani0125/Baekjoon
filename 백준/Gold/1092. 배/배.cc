#include <bits/stdc++.h>

using namespace std;

int BinarySearch(const vector<int> &v, const int &t)
{
    int low = 0, high = v.size() - 1, mid;
    while (low <= high)
    {
        mid = (low + high) / 2;
        if (t >= v[mid])
        {
            high = mid - 1;
        }
        else
        {
            low = mid + 1;
        }
    }
    return low;
}

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n, m;

    cin >> n;
    vector<int> a(n);
    for (auto &i : a) cin >> i;

    cin >> m;
    vector<int> b(m);
    for (auto &i : b) cin >> i;

    sort(a.begin(), a.end(), greater<int>());
    sort(b.begin(), b.end(), greater<int>());

    if (a[0] < b[0])
    {
        cout << -1;
        return 0;
    }

    queue<pair<int, pair<int, int>>> q;
    for (auto i : a)
    {
        q.push({0, {i, BinarySearch(b, i)}});
    }

    vector<bool> visited(m + 1, false);
    
    int nc, na, nb, ans = 0;
    while (!q.empty())
    {
        nc = q.front().first;
        na = q.front().second.first;
        nb = q.front().second.second;
        q.pop();

        while (visited[nb]) nb++;
        
        if (nb == m)
        {
            ans = max(ans, nc);
        }
        else
        {
            visited[nb] = true;
            q.push({nc + 1, {nb, nb}});
        }
    }
    
    cout << ans;
    
    return 0;
}
