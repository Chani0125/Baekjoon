#include <bits/stdc++.h>

using namespace std;

const int d[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int main(void)
{
    // ios_base::sync_with_stdio(0);
    // cin.tie(0);

    int t; cin >> t;
    while (t--)
    {
        int n, m;
        cin >> n >> m;

        string str;
        pair<int, int> exit_pos;

        vector<vector<int>> v(n, vector<int> (m));
        for (int i = 0; i < n; i++)
        {
            cin >> str;
            for (int j = 0; j < m; j++)
            {
                if (str[j] == '#')
                    v[i][j] = 0;
                else if (str[j] == 'O')
                {
                    v[i][j] = 1;
                    exit_pos = {i, j};
                }
                else
                    v[i][j] = 2;
            }
        }

        queue<pair<int, pair<int, int>>> q;
        q.push({0, exit_pos});

        int cnt, x, y, nx, ny, pass;
        while (!q.empty())
        {
            cnt = q.front().first;
            x = q.front().second.first;
            y = q.front().second.second;
            q.pop();

            if (cnt == 10)
                break;

            for (int i = 0; i < 4; i++)
            {
                pass = 0;
                nx = x + d[i][0];
                ny = y + d[i][1];

                while (v[nx+d[i][0]][ny+d[i][1]] > 0)
                {
                    if (nx == exit_pos.first && ny == exit_pos.second)
                    {
                        pass = 1;
                        break;
                    }
                    v[nx][ny] = 3 + cnt;
                    nx += d[i][0];
                    ny += d[i][1];
                }

                if (pass == 1) continue;
                
                if (nx != x || ny != y)
                {
                    if (v[nx][ny] < 4 + cnt)
                    {
                        v[nx][ny] = 4 + cnt;
                        q.push({cnt+1, {nx, ny}});
                    }
                }
            }

            for (auto i : v)
            {
                for (auto j : i)
                    cout << j << " ";
                cout << "\n";
            }
            cout << "\n";            
        }

        for (auto i : v)
        {
            for (auto j : i)
                cout << j << " ";
            cout << "\n";
        }

    }

    return 0;
}