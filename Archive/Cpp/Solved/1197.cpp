#include <bits/stdc++.h>

#define INF INT_MAX
#define ll long long
#define vvp vector<vector<pair<ll, int>>>
#define vp vector<pair<ll, int>>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int v, e;
    cin >> v >> e;

    int a, b, c;
    vvp edges(v+1);
    for (int i = 0; i < e; i++)
    {
        cin >> a >> b >> c;
        edges[a].push_back({b, c});
        edges[b].push_back({a, c});
    }

    vector<ll> cost(v+1, INF);
    vector<bool> visited(v+1, false);
    priority_queue<pair<ll, int>, vp, greater<>> pq;
    pq.push({0, 1});
    cost[1] = 0;

    int node; ll weight;
    while (!pq.empty())
    {
        node = pq.top().second;
        weight = pq.top().first;
        pq.pop();

        if (visited[node]) continue;
        visited[node] = true;

        for (auto &next : edges[node])
        {
            if (!visited[next.first] && next.second < cost[next.first])
            {
                cost[next.first] = next.second;
                pq.push({cost[next.first], next.first});
            }
        }
    }

    ll ans = 0;
    for (int i = 1; i <= v; i++)
    {
        ans += cost[i];
    }
    cout << ans << "\n";

    return 0;
}
