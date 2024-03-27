#include <bits/stdc++.h>

#define INF __INT_MAX__

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n, m, x;
    cin >> n >> m >> x;

    vector<vector<pair<int, int>>> adj(n);
    int s, e, t;
    for (int i = 0; i < m; i++)
    {
        cin >> s >> e >> t;
        adj[s-1].push_back({e-1, t});
    }
    
    vector<int> dist_from_x(n, INF);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
    pq.push({0, x-1});
    dist_from_x[x-1] = 0;

    int curr, cost;
    while (!pq.empty())
    {
        cost = pq.top().first;
        curr = pq.top().second;
        pq.pop();

        if (cost > dist_from_x[curr]) continue;

        for (auto &next : adj[curr])
        {
            if (cost + next.second < dist_from_x[next.first])
            {
                dist_from_x[next.first] = cost + next.second;
                pq.push({dist_from_x[next.first], next.first});
            }
        }
    }

    vector<int> dist_to_x(n, 0);

    for (int i = 0; i < n; i++)
    {
        if (i == x-1) continue;

        vector<int> dist(n, INF);
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
        pq.push({0, i});
        dist[i] = 0;

        int curr, cost;
        while (!pq.empty())
        {
            cost = pq.top().first;
            curr = pq.top().second;
            pq.pop();

            if (cost > dist[curr]) continue;

            for (auto &next : adj[curr])
            {
                if (cost + next.second < dist[next.first])
                {
                    dist[next.first] = cost + next.second;
                    pq.push({dist[next.first], next.first});
                }
            }
        }

        dist_to_x[i] = dist[x-1];
    }

    vector<int> dist(n);
    for (int i = 0; i < n; i++)
    {
        dist[i] = dist_from_x[i] + dist_to_x[i];
    }

    cout << *max_element(dist.begin(), dist.end()) << "\n";
    

    return 0;
}
