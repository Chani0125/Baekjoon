#include <bits/stdc++.h>

#define INF INT_MAX

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int v, e;
    cin >> v >> e;

    int k; cin >> k;

    int a, b, w;
    vector<vector<pair<int, int>>> m(v);
    for (int i = 0; i < e; i++)
    {
        cin >> a >> b >> w;
        m[a-1].push_back({b-1, w});
    }

    vector<int> d(v, INF);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
    pq.push({0, k-1});
    d[k-1] = 0;

    int curr, dist;
    while (!pq.empty())
    {
        dist = pq.top().first;
        curr = pq.top().second;
        pq.pop();

        if (dist > d[curr]) continue;

        for (auto &next : m[curr])
        {
            if (dist + next.second < d[next.first])
            {
                d[next.first] = dist + next.second;
                pq.push({dist + next.second, next.first});
            }
        }
    }

    for (auto &ans : d)
    {
        if (ans == INF) 
        {
            cout << "INF\n";
        }
        else
        {
            cout << ans << "\n";
        }
    }
    
    return 0;
}
