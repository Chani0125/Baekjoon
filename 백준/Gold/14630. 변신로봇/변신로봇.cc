#include <iostream>
#include <queue>
#include <vector>

#define INF 1e9

using namespace std;

int main(void) {
    int n;
    cin >> n;
    char robots[n][101];
    for (int i = 0; i < n; i++) cin >> robots[i];

    int graph[n][n] = {};
    for (int i = 0; i < n; i++) {
        for (int j = i+1; j < n; j++) {
            int cost = 0;
            for (char *from = robots[i], *to = robots[j]; *from != 0; from++, to++) {
                cost += (*from - *to) * (*from - *to);
            }
            graph[i][j] = graph[j][i] = cost;
        }
    }

    // for (int i = 0; i < n; i++) {
    //     for (int j = 0; j < n; j++) cout << graph[i][j] << " ";
    //     cout << endl;
    // }

    int start, end;
    cin >> start >> end ;
    bool visited[n] = {};
    int to_cost[n];
    fill(to_cost, to_cost+n, INF);

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    visited[start-1] = true;
    to_cost[start-1] = 0;
    pq.push({0, start-1});

    while (!pq.empty()) {
        int dist = pq.top().first;
        int now = pq.top().second;
        pq.pop();

        if (dist > to_cost[now]) continue;

        for (int i = 0; i < n; i++) {
            if (graph[now][i]) {
                int cost = dist + graph[now][i];
                if (cost < to_cost[i]) {
                    to_cost[i] = cost;
                    pq.push({cost, i});
                }
            }
        }
    }

    // for (int i = 0; i < n; i++) cout << to_cost[i] << " ";
    // cout << endl;

    cout << to_cost[end-1] << endl;

    return 0;
}