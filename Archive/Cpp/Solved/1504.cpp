#include <bits/stdc++.h>

#define ll long long
#define INF INT_MAX

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n, e;
    cin >> n >> e;

    vector<vector<pair<int, int>>> road(n+1);
    int u, v, c;
    for (int i = 0; i < e; i++)
    {
        cin >> u >> v >> c;
        road[u].push_back({v, c});
        road[v].push_back({u, c});
    }
    
    int vv[] = {1, 0, 0};
    cin >> vv[1] >> vv[2];

    vector<vector<int>> dist(3, vector<int>(n+1, INF));
    priority_queue<pair<int, ll>, vector<pair<int, ll>>, greater<>> pq;

    for (int i = 0; i < 3; i++)
    {
        pq.push({0, vv[i]});
        dist[i][vv[i]] = 0;

        int curr; ll cost;
        while (!pq.empty())
        {
            cost = pq.top().first;
            curr = pq.top().second;
            pq.pop();

            if (cost > dist[i][curr]) continue;
            
            for (auto &next : road[curr])
            {   
                if (cost + next.second < dist[i][next.first])
                {
                    dist[i][next.first] = cost + next.second;
                    pq.push({dist[i][next.first], next.first});
                }
            }
        }
    }

    int ans, ans0 = INF, ans1 = INF;
    if (dist[0][vv[1]] != INF && dist[1][vv[2]] != INF && dist[2][n] != INF)
    {
        ans0 = dist[0][vv[1]] + dist[1][vv[2]] + dist[2][n];
    }
    if (dist[0][vv[2]] != INF && dist[2][vv[1]] != INF && dist[1][n] != INF)
    {
        ans1 = dist[0][vv[2]] + dist[2][vv[1]] + dist[1][n];
    }

    ans = min(ans0, ans1);
    if (ans == INF) ans = -1;
    cout << ans << "\n";
    
    return 0;
}
