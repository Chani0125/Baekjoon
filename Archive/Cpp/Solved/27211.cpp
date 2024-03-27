#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int n, m, tmp;
    cin >> n >> m;

    vector<vector<int>> v(n, vector<int>(m));
    int cnt_true = 2;
    deque<pair<int, int>> q;

    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
        {
            cin >> tmp;
            if (tmp == 0)
            {
                tmp = cnt_true++;
                q.push_back({i, j});
            }
            v[i][j] = tmp;
        }
        
    int x, y, dx, dy, now, nx, ny;
    int d[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

    while(!q.empty())
    {
        x = q.front().first;
        y = q.front().second;
        q.pop_front();

        now = v[x][y];
        for (int i = 0; i < 4; i++)
        {
            nx = (x+d[i][0]+n) % n;
            ny = (y+d[i][1]+m) % m;

            if (v[nx][ny] != 1 && v[nx][ny] > now)
            {
                v[nx][ny] = now;
                q.push_front({nx, ny});
            }
        }
    }


    int ans = 0;
    cnt_true = 1;
    for (auto i : v)
    {
        for (auto j : i)
            if (j > cnt_true)
            {   
                // cout << j << " ";
                cnt_true = j;
                ans++;
            }
        // cout << "\n";
    }

    cout << ans << "\n";

    return 0;
}