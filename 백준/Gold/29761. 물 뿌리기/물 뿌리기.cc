#include <bits/stdc++.h>

using namespace std;

int d[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

bool CheckRangeIn(int x, int y, int n)
{
    if (0 <= x && x < n)
        if (0 <= y && y < n)
            return true;
    return false;
}

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n, s, x, y;
    cin >> n >> s >> x >> y;

    vector<vector<int>> m(n, vector<int>(n));
    vector<vector<int>> w(n, vector<int>(n));
    w[x-1][y-1] = s;

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> m[i][j];
    
    priority_queue<pair<int, pair<int, int>>> pq;
    pq.push({m[x-1][y-1], {x-1, y-1}});

    int h, nx, ny, dx, dy;
    while(!pq.empty())
    {
        h = pq.top().first;
        nx = pq.top().second.first;
        ny = pq.top().second.second;
        pq.pop();

        for (int i = 0; i < 4; i++)
        {
            dx = nx + d[i][0];
            dy = ny + d[i][1];

            if (CheckRangeIn(dx, dy, n) && w[nx][ny] > 1)
            {
                if (m[dx][dy] == h)
                {
                    if (w[dx][dy] < w[nx][ny] - 1)
                    {
                        w[dx][dy] = w[nx][ny] - 1;
                        pq.push({m[dx][dy], {dx, dy}});
                    }
                }
                else if (m[dx][dy] < h)
                {
                    if (w[dx][dy] < s)
                    {
                        w[dx][dy] = s;
                        pq.push({m[dx][dy], {dx, dy}});
                    }
                }
            }
        }
    }

    int ans = 0;
    for (auto i : w)
        for (auto j : i)
            if (j > 0) ans++;

    cout << ans;

    return 0;
}
