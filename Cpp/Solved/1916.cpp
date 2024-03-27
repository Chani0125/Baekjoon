#include <bits/stdc++.h>

#define INF INT_MAX

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n, m;
    cin >> n >> m;

    int a, b, w;
    vector<vector<pair<int, int>>> bus(n);
    for (int i = 0; i < m; i++)
    {
        cin >> a >> b >> w;
        bus[a-1].push_back({b-1, w});
    }

    int s, e;
    cin >> s >> e;

    vector<int> d(n, INF);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
    pq.push({0, s-1});
    d[s-1] = 0;

    int curr, dist;
    while (!pq.empty())
    {
        dist = pq.top().first;
        curr = pq.top().second;
        pq.pop();

        if (dist > d[curr]) continue;

        for (auto &next : bus[curr])
        {
            if (dist + next.second < d[next.first])
            {
                d[next.first] = dist + next.second;
                pq.push({dist + next.second, next.first});
            }
        }
    }

    cout << d[e-1] << "\n";

    return 0;
}
