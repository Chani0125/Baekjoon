#include <bits/stdc++.h>

using namespace std;

int d[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int n, m;
    cin >> n >> m;

    string str;
    
    vector<vector<int>> v(n, vector<int>(m));
    for (int i = 0; i < n; i ++)
    {
        cin >> str;
        for (int j = 0; j < m; j++)
            v[i][j] = (str[j] == '.');
    }

    int r, c;
    pair<int, int> p1, p2;
    
    cin >> r >> c;
    p1.first = r-1; p1.second = c-1;
    cin >> r >> c;
    p2.first = r-1; p2.second = c-1;

    queue<pair<int, int>> q;

    v[p1.first][p1.second] = 1;
    q.push(p1);

    int x, y, nx, ny, ans = 0;
    while (!q.empty())
    {
        x = q.front().first;
        y = q.front().second;
        q.pop();

        if (v[x][y] == 0)
        {
            if (x == p2.first && y == p2.second)
            {
                ans = 1;
                break;
            }
            else
                continue;
        }
        
        v[x][y]--;

        for (int i = 0; i < 4; i++)
        {
            nx = x + d[i][0];
            ny = y + d[i][1];
            if (0 <= nx && nx < n && 0 <= ny && ny < m)
            {
                q.emplace(nx, ny);
            }
        }
    }

    if (ans == 1) cout << "YES\n";
    else cout << "NO\n";

    return 0;
}